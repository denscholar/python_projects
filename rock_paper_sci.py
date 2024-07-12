from enum import Enum
import random
import sys


class Rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(Rps(1))
# print(Rps(2))
# print(Rps(3))

# sys.exit()


your_choice = int(input("Choose a number between 1 and 3. E.g 1, 2, or 3 \n"))
computer_choice = random.choice([1, 2, 3])

print("You selected:", str(Rps(your_choice)).replace("Rps.", ""))
print("Computer selected:", str(Rps(computer_choice)).replace("Rps.", ""))


while your_choice <= 0 or your_choice >= 4:
    your_choice = int(
        input("Invalid number, choose a number between 1 and 3. E.g 1, 2, or 3 \n")
    )

if your_choice == 1 and computer_choice == 3:
    print("You won the game")
elif your_choice == 2 and computer_choice == 1:
    print("Python won!!!")
elif your_choice == 3 and computer_choice == 2:
    print("You won the game")
elif your_choice == computer_choice:
    print("Tie Game!")
else:
    f"Python Wins!!!"
