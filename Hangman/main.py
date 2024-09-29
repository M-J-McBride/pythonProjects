from random import choice
def run_game():
    word: str = choice(['apple','secret','banana','thirty'])
    user_name: str = input("What is your name? >> ")
    print(f"Welcome to hangman, {user_name}!")

    # Setup
    guessed: str = ""
    tries: int = 3

    while tries > 0:
        blanks: int = 0
        print(f"Word: ", end='')
        for char in word:
            if char in guessed:
                print(char, end = '')
            else:
                print('_', end='')
                blanks += 1

        print() # Adds a blank line
        print() # Adds a blank line
        if blanks == 0:
            print("You won!")
            break

        new_guess: str = input("Guess a letter: ")
        if new_guess in guessed:
            print("You already guessed that!")
            continue
        elif len(new_guess) >1:
            if new_guess == word:
                print("You guessed the word!")
                break
            else:
                tries -= 1
                print(f"That is not the word! You have {tries} tries left.")
                continue


        guessed += new_guess

        if new_guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong. You have {tries} tries left.")

            if tries == 0:
                print("No more tries remaining, you lose")
                break


if __name__ == '__main__':
    run_game()