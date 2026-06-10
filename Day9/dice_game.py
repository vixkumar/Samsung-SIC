import random
import time

def roll_dice(n):
    dice = []

    for i in range(n):
        dice.append(random.randint(1, 6))

    return dice


def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)

    print("Computer Total", computer_total)
    print("User Total", user_total)

    if user_total > computer_total:
        print("User wins")
    elif user_total < computer_total:
        print("Computer wins")
    else:
        print("It is a tie")


def roll_again(choices, dice_list):
    print("Rolling again...")
    time.sleep(3)

    for i in range(len(dice_list)):
        if choices[i] == "r":
            dice_list[i] = random.randint(1, 6)

    time.sleep(3)


def computer_strategy1(n):
    print("Computer is thinking")
    time.sleep(3)

    choices = ""

    for i in range(n):
        choices += "r"

    return choices


def computer_strategy2(dice_list):
    print("Computer is thinking")
    time.sleep(3)

    choices = ""

    for value in dice_list:
        if value < 5:
            choices += "r"
        else:
            choices += "-"

    return choices


number_dice = int(input("Enter number of dice: "))

input("Ready to start? Hit any key to continue ")

user_rolls = roll_dice(number_dice)
print("User first roll:", user_rolls)

user_choices = input("Enter - to hold or r to roll again: ")

while (len(user_choices) != number_dice or
       any(choice not in "-r" for choice in user_choices)):
    print("You must enter exactly", number_dice,
          "characters using only '-' or 'r'")
    user_choices = input("Enter - to hold or r to roll again: ")

roll_again(user_choices, user_rolls)
print("Player new roll:", user_rolls)

print("Computer turn")

computer_rolls = roll_dice(number_dice)
print("Computer first roll:", computer_rolls)

computer_choices = computer_strategy2(computer_rolls)
print("Computer choice:", computer_choices)

roll_again(computer_choices, computer_rolls)
print("Computer new roll:", computer_rolls)

find_winner(computer_rolls, user_rolls)
