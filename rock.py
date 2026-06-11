import random
choices = ["rock", "paper", "scissors"]
while True:
    com = random.choice(choices)
    guess = input("Choose rock, paper, or scissors: ").lower()
    if guess not in choices:
        print("Invalid choice!")
        continue
    print("Computer chose:", com)
    if guess == com:
        print("It's a tie!")
    elif (
        (guess == "rock" and com == "scissors") or
        (guess == "paper" and com == "rock") or
        (guess == "scissors" and com == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break