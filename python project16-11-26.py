
import random

user = 0
computer = 0

while True:
    a = input("Enter rock, paper or scissors : ")

    if a == "quit":
        break

    b = random.choice(["rock", "paper", "scissors"])

    print("Computer chose:", b)

    if a == b:
        print("Tie")

    elif a == "rock" and b == "scissors":
        print("You win")
        user = user + 1

    elif a == "paper" and b == "rock":
        print("You win")
        user = user + 1

    elif a == "scissors" and b == "paper":
        print("You win")
        user = user + 1

    else:
        print("Computer wins")
        computer = computer + 1

    print("Your score:", user)
    print("Computer score:", computer)

print("Final score")
print("Your score:", user)
print("Computer score:", computer)
