import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()
    
random_number = random.randint(0, top_of_range)
guess_count = 0

while True:
    user_guess = input("Make a guess: ")
    guess_count += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        print("You used " + str(guess_count) + " guesses")
        break
    elif user_guess > random_number:
        print("You were above the number!")
        print("You have used", guess_count, "guesses so far")
    else:
        print("You were below the number!")
        print("You have used", guess_count, "guesses so far")
    

