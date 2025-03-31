import math

def square_root(x):

    if x < 0:
        raise ValueError("Square root of a negative number is not allowed.")
    return math.sqrt(x)

def factorial(x):

    if x < 0:
        raise ValueError("Factorial of a negative number is not defined.")
    return math.factorial(x)

def natural_log(x):

    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(x)

def power(x, b):

    if x < 0 and b % 1 != 0:
        raise ValueError("Negative base with a fractional exponent is not allowed.")
    return math.pow(x, b)

def main():
    while True:
        print("\n" + "=" * 35)
        print("      SCIENTIFIC CALCULATOR")
        print("=" * 35)
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")
        print("=" * 35)

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                x = float(input("Enter a number: "))
                result = square_root(x)
                print(f"√{x} = \033[1;92m{result:.4f}\033[0m")

            elif choice == '2':
                x = int(input("Enter a non-negative integer: "))
                result = factorial(x)
                print(f"{x}! = \033[1;92m{result}\033[0m")

            elif choice == '3':
                x = float(input("Enter a positive number: "))
                result = natural_log(x)
                print(f"ln({x}) = \033[1;92m{result:.4f}\033[0m")

            elif choice == '4':
                x = float(input("Enter the base: "))
                b = float(input("Enter the exponent: "))
                result = power(x, b)
                print(f"{x}^{b} = \033[1;92m{result:.4f}\033[0m")

            elif choice == '5':
                print("\n\033[1;91mExiting calculator. Goodbye!\033[0m")
                break

            else:
                print("\033[1;91mInvalid choice! Please enter a number between 1 and 5.\033[0m")

        except ValueError as e:
            print(f"\033[1;91mError: {e}\033[0m")

if __name__ == "__main__":
    main()
#helo
