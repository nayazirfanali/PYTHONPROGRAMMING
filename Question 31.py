def calculate_power(x, n):
    return x ** n

def calculate_addition(x, n):
    return x + n

def calculate_subtraction(x, n):
    return x - n

def calculate_multiplication(x, n):
    return x * n

def calculate_division(x, n):
    if n == 0:
        return "Cannot divide by zero"
    return x / n

def main():
    x = float(input("Enter the value of x: "))
    n = float(input("Enter the value of n: "))
    choice = input("Enter the operation to perform (power/add/sub/mul/div): ")

    if choice == "power":
        result = calculate_power(x, n)
    elif choice == "add":
        result = calculate_addition(x, n)
    elif choice == "sub":
        result = calculate_subtraction(x, n)
    elif choice == "mul":
        result = calculate_multiplication(x, n)
    elif choice == "div":
        result = calculate_division(x, n)
    else:
        result = "Invalid choice"

    print("Result:", result)

if __name__ == "__main__":
    main()


