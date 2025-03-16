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
    clear_screen()
    
    try_count = 3
    print(f"You have {try_count} tries.")

    magic_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"MAGIC NUMBER {magic_number}")

    player_number = get_player_guess()
    while magic_number != player_number:
        try_count -= 1
        if try_count == 0:
            break

        print(f"Wrong guess! You have {try_count} tries left.")
        player_number = get_player_guess()
    
    # End game condition
    if magic_number == player_number:
        print(f"You win. My number was {magic_number}")
    else:
        print("You lost this round :(")
    
    result = ask_player("Do you want to play again?")
    if result == "y":
        game_loop()
    else:
        exit_game()

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
        result = input("What is your guess? ")

    return int(result)

main()