import random, os, time

MIN_NUMBER = 1
MAX_NUMBER = 10

def main():
    clear_screen()
    intro()

    time.sleep(5)

    clear_screen()

    result = input("Are you ready?")
    if result == "y":
        game_loop()

    clear_screen()
    exit_game()

def intro():
    print("-"*50, "The Magic Number Game", "-"*50)
    print(f"I think of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")

def clear_screen():
    pass

def game_loop():
    pass

def exit_game():
    pass

main()