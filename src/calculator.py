from src.utils import add, subtract, multiply, divide


def calculator():
    """Simple interactive calculator."""
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Choose an operation (1–5): ")

        if choice == "5":
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            else:
                print("Invalid choice, please try again.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("❌ Invalid input, please enter numbers only.")
        except ZeroDivisionError:
            print("❌ Cannot divide by zero.")

        again = input("Do you want another calculation? (y/n): ").lower()
        if again != "y":
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
