name = input("Type your name: ")
print("Welcome", name ,"to this adventure!")

answer = input(
    "Do you want to be born as a Saiyan or a Hybrid? ").lower()

if "saiyan" in answer:
    answer = input(
        "Learn kaioken or kamehameha: ").lower()
    if answer == "kaioken":
        print("Congrats! Thanks to this decision, you defeated Jiren!")
    elif answer == "kamehameha":
        print("Unfortunately your Kamehameha wasn't enough to take down Jiren and you lost the decisive battle.")
    else:
        print('Not a valid option. You lose.')

elif answer == "hybrid":
    answer = input(
        "Train or Study: ").lower()
    if answer == "train":
        print("OMG YOU ARE THE STRONGEST AND THE MOST POWERFUL BEING IN THE EXISTENCE!")
    elif answer == "study":
        print("You are all-knowing, can do any job out there in the world and are rich but you are far from the strongest or the more powerful being in the existence.")
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')
