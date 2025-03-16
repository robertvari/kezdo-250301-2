import random, os, time

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
    pass

def clear_screen():
    pass

def game_loop():
    pass

def exit_game():
    pass

main()