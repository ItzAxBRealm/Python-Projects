name = input("Type your name: ")
print("Welcome", name ,"to this adventure!")

answer = input(
    "Do you want to be born as an Uchiha or a Uzumaki? ").lower()

if answer == "uchiha":
    answer = input(
        "Learn genjutsu or chidori: ").lower()
    if answer == "genjutsu":
        print("Congrats! Thanks to this decision, you defeated Itachi!")
        answer = input("Just kidding. You are under Itachi's genjutsu.\nItachi leaves, Pain attacks Konoha, Do you join the Akatsuki or Fight Pain? ").lower()
        if answer == "akatsuki":
            print("Everyone in the village hates you but you have become the strongest in the world through Akatsuki's help.")
        elif "fight" in answer:
            print("You have defeated Pain and become the hero of Konoha but you will have to rise in strength on your own without Akatsuki's help.")
        else:
            print("Not a valid option. You Lose.")
    elif answer == "chidori":
        print("Thanks to your chidori, you won your chunin fight against Gaara.")
        answer = input("Orochimaru attacks, type \"join\" to join his side and \"stay\" to stay on Konoha's side: ").lower()
        if answer == "join":
            print("You have become a rogue ninja and managed to gain a lot of power but the villages hates you and you lost your friends.")
        elif answer == "stay":
            print("You aren't that strong but you manage to still have your friends and your village loves you.")
        else:
            print("Not a valid option. You Lose.")
    else:
        print('Not a valid option. You lose.')

elif answer == "uzumaki":
    answer = input(
        "learn rasengan or shadow clones? : ").lower()
    if "shadow" in answer or "clones" in answer:
        print("You just beat Neji in your chunin exam using Shadow clones.")
    elif answer == "rasengan":
        print("You tried to rasengan Madara but he easily countered it with his susano.")
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')
