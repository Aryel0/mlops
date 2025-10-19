from src.utils import add, subtract, multiply, divide

def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please try again.")
            continue  # or return to stop immediately

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input.")
            continue

        try:
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)

            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Do you want another calculation? (y/n): ")
        if again.lower() != "y":
            print("Goodbye!")
            break
