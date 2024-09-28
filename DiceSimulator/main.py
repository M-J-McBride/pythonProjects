import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        rolls.append(random.randint(1,6))
    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll?: ")

            if user_input.lower() == 'exit':
                print("Goodbye and thanks for playing!")
                break
            roll_results: list[int] = roll_dice(int(user_input))
            print(*roll_results, sep=', ')
            print(f"Total: {sum(roll_results)}")
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")

if __name__ == "__main__":
    main()