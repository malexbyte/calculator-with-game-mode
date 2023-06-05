import random

# Define a function to perform basic arithmetic calculations
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None

# Define a function to play a number guessing game
def game():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        if guess == 'q':
            print("Thanks for playing!")
            break
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations, you guessed the number!")
            break

# Main program loop
while True:
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Play game")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == '6':
        print("Goodbye!")
        break
    elif choice == '5':
        game()
        continue
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue
    if choice == '1':
        operator = '+'
    elif choice == '2':
        operator = '-'
    elif choice == '3':
        operator = '*'
    elif choice == '4':
        operator = '/'
    else:
        print("Invalid choice.")
        continue
    result = calculate(num1, operator, num2)
    if result is None:
        print("Invalid operator.")
    else:
        print(f"{num1} {operator} {num2} = {result}")
