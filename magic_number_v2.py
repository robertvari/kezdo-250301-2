import random, os, time

MIN_NUMBER = 1
MAX_NUMBER = 10

def main():
    clear_screen()
    intro()

    time.sleep(2)

    result = ask_player("Are you ready?")
    if result == "y":
        game_loop()

    exit_game()

def intro():
    print("-"*50, "The Magic Number Game", "-"*50)
    print(f"I think of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def game_loop():
    pass

def exit_game():
    clear_screen()
    print("Thank you for playing my game :))) See you next time!")

def ask_player(question):
    result = input(f"{question} (y/n)")

    valid_characters = "yn"

    while result not in valid_characters:
        clear_screen()
        print("Wrong answer. Only use y/n.")
        result = input(f"{question} (y/n)")
    
    return result

main()