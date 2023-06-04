import random
def fun():
    my_action = input("Enter a choice (rock, paper, scissors): ")
    computer_actions = ["rock", "paper", "scissors"]
    computer = random.choice(computer_actions)
    
    if my_action == computer:
        print(f"\nYou chose {my_action}, computer chose {computer}.\n")
        print(f"Both actions are same")
    elif my_action == "rock":
        if computer == "scissors":
            print(f"\nYou chose {my_action}, computer chose {computer}.\n")
            print("Rock smashes scissors! You win!")
        else:
            print(f"\nYou chose {my_action}, computer chose {computer}.\n")
            print("Paper covers rock! You lose.")
    elif my_action == "paper":
        if computer == "scissors":
            print(f"\nYou chose {my_action}, computer chose {computer}.\n")
            print("Scissors cuts paper! You lose.")
        else:
            print(f"\nYou chose {my_action}, computer chose {computer}.\n")
            print("Paper covers rock! You win!")
    elif my_action == "scissors":
        if computer == "paper":
            print(f"\nYou chose {my_action}, computer chose {computer}.\n")
            print("Scissors cuts paper! You win!")
        else:
            print(f"\nYou chose {my_action}, computer chose {computer}.\n")
            print("Rock smashes scissors! You lose.")
    else:
        print("invalid output")
fun()
play_again=input("do you want to play again(yes/no):")
while play_again=="yes":
    fun()
    play_again=input("do you want to play again(yes/no):")
else:
    print("thankyou")

            
