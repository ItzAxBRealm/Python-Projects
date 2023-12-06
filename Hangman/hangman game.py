from art import logo
from wordlist import word_list
from art import stages
import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = len(stages) - 1

display = []
for _ in range(word_length):
  display += "_"

game_over = False
print(logo)
while not game_over:
  guess = input("Guess a letter: ").lower()
  
  if guess in display:
    print("You have already guessed " + guess + "' before")
  elif guess in chosen_word:
    print("You guessed the letter " + guess + ". You got it correct.")
  elif not guess in chosen_word:
    print("You guessed the letter " + guess + ". It's not part of the word so you lose a life.")
  
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter     
    
  print(f"{' '.join(display)}") 
     
  if guess not in chosen_word:
    lives -= 1

  if "_" not in display:
    game_over = True
    print("You win")
  elif lives == 0:
    game_over = True
    print("You lose, the chosen word was " + chosen_word)
  
  print(stages[lives])