
import random
import time
from unittest import case


def get_user_choice() -> str:
    while True:
        user = input("please write your choose correctly: rock 🪨, paper 📄 or scissors ✂️. ")
        if user == "rock":
            return "🪨"
        elif user == "paper":
            return "📄"
        elif user == "scissors":
            return "✂️"
        else:
            print("please write your choose correctly")
            continue

def get_random_computer_choice() -> str:
    match random.choice(["rock", "paper", "scissors"]):
        case "rock":
            return "🪨"
        case "paper":
            return "📄"
        case "scissors":
            return "✂️"
        case _:
            return None

def print_user_choice_icon_and_delay(choice, how_long_sleep) -> None:
    print(choice)
    time.sleep(how_long_sleep)

def print_computer_choice_icon(choice) -> None:
    print(choice)

def get_game_result(user_choice, computer_choice) -> str:
    ver1 = {("🪨", "✂️"), ("📄", "🪨"), ("✂️", "📄")}
    ver2 = {("✂️", "🪨"), ("🪨", "📄"), ("📄", "✂️")}
    if (user_choice, computer_choice) in ver1:
        return "user wins"
    if (user_choice,computer_choice) in ver2:
        return "computer wins"
    else:
        return "draw"

def print_result_and_icon(get_result) -> None:
    """
    👋 💥🤝✅
    Print result with icon
    :param get_result: str winner - 'user', 'draw', 'computer'
    :return: None
    """
    if get_result == "user wins":
        print("you won ✅")
    if get_result == "draw":
        print("it is draw 🤝")
    if get_result == "computer wins":
        print("PC smash you human 💥")

# Icons for each choice
ICONS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}

print("🎮 Rock–Paper–Scissors")

user_choice = get_user_choice()
print_user_choice_icon_and_delay(user_choice,1)
computer_choice = get_random_computer_choice()
print_computer_choice_icon(computer_choice)
get_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(get_result)