import random

while True:

    user_actions=input("Enter your choice (Stone,Paper,Scissors) : ")
    possible_actions=["Stone","Paper","Scissors"]
    computer_actions=random.choice(possible_actions)
    print(f"\n Your Choice {user_actions}, Computer Choice {computer_actions}")

    if user_actions==computer_actions:
        print(f"Both Selected {user_actions}, TIE")
    elif user_actions=="Stone":
        if computer_actions=="Paper":
           print("Paper covers Stone, YOU LOSE")
        else:
           print("Stone Breaks Scissors, YOU WIN")
    elif user_actions=="Paper":
        if computer_actions=="Stone":
            print("Paper covers Stone, YOU WIN ")
        else:
            print("Paper got cut by Scissors, YOU LOSE")
    elif user_actions=="Scissors":
        if computer_actions=="Stone":
             print("Scissors got smashed by Stone, YOU LOSE")
        else:
             print("Scissors cut Papers, YOU WON")

    play_again = input("Play Again? (y/n):")
    if play_again.lower() != "y":
      break



