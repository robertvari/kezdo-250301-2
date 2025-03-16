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
    try_count = 3
    print(f"You have {try_count} tries.")

    magic_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"MAGIC NUMBER_ {magic_number}")

    player_number = get_player_guess()

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

def get_player_guess():
    result = input("What is your guess? ")

    valid_numbers = "12345678910"

    while result not in valid_numbers:
        print("Wrong number.")
        get_player_guess()

    return int(result)

main()