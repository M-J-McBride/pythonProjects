from random import randint

lower_num, higher_num = 1, 10

random_number: int = randint(lower_num, higher_num)

print(f"Guess the number in the range from {lower_num} to {higher_num}.")
count = 0
while True:
    try:
        user_input: int = int(input("Enter your guess: "))
    except ValueError as e:
        print("Please enter a valid number.")
        continue

    if count >= 3:
        print(f"You have reached the maximum number of attempts. The number was {random_number}.")
        break
    elif user_input > random_number:
        print("The number is lower")
        count += 1
    elif user_input < random_number:
        print("The number is higher")
        count += 1
    else:
        print("You guessed it right!")
        break
