import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    while True:
        print("\n" + "="*35)
        print("      SCIENTIFIC CALCULATOR")
        print("="*35)
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")
        print("="*35)

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            x = float(input("Enter a number: "))
            print(f"√{x} = \033[1;92m{square_root(x):.4f}\033[0m")
        elif choice == '2':
            x = int(input("Enter a number: "))
            print(f"{x}! = \033[1;92m{factorial(x)}\033[0m")
        elif choice == '3':
            x = float(input("Enter a number: "))
            print(f"ln({x}) = \033[1;92m{natural_log(x):.4f}\033[0m")
        elif choice == '4':
            x = float(input("Enter the base: "))
            b = float(input("Enter the exponent: "))
            print(f"{x}^{b} = \033[1;92m{power(x, b):.4f}\033[0m")
        elif choice == '5':
            print("\n\033[1;91mExiting calculator. Goodbye!\033[0m")
            break
        else:
            print("\033[1;91mInvalid choice! Please enter a number between 1 and 5.\033[0m")

if __name__ == "__main__":
    main()
