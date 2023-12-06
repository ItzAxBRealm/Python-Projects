import random


def all_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(users_score, cpus_score):
  if users_score == cpus_score:
    return "Draw!"
  elif cpus_score == 0:
    return "You lose, Computer got a blackjack!"
  elif users_score == 0:
    return "You win, you got a Blackjack!"
  elif users_score > 21:
    return "You lose, your score went past 21!"
  elif cpus_score > 21:
    return "You win, computer score went past 21!"
  elif users_score > cpus_score:
    return "You win!"
  else:
    return "You lose!"
    
  

def blackjack():
  user_cards = []
  computer_cards = []
  game_over = False
  
  for _ in range(2):
    user_cards.append(all_cards())
    computer_cards.append(all_cards())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    cpu_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or cpu_score == 0 or user_score > 21:
      game_over = True
    else:
      card3 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if card3 == "y":
        user_cards.append(all_cards())
      else:
        game_over = True
  
  while cpu_score != 0 and cpu_score < 17:
    computer_cards.append(all_cards())
    cpu_score = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, your final score is {user_score}")
  print(f"Computer's final hand: {computer_cards}, computer's final score is: {cpu_score}")
  print(compare(user_score, cpu_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  blackjack()