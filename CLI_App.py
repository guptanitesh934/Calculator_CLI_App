# --- Mathematical Functions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed"
    return a / b


# --- Main Application Loop ---
print("=====Welcome to Calculator CLI App=====\n")

while True:
    # Taking input from user
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("\n")
    
    x = input("Enter the Mathematical Operator (+, -, *, /): ")
    print("\n")

    # Routing to the correct function based on the operator
    if x == "+":
        print(a, "+", b, "=", add(a, b))

    elif x == "-":
        print(a, "-", b, "=", subtract(a, b))

    elif x == "*":
        print(a, "*", b, "=", multiply(a, b))

    elif x == "/":
        print(a, "/", b, "=", divide(a,b))

    else:
        print("No match found! Please Enter Valid Input")

    # Prompting the user to continue or exit
    print("\n")
    choice = input("Do you want to exit the calculator? (y/n): ").strip().lower()
    
    if choice == 'y':
        print("Exiting Calculator. Goodbye!")
        break
    
    print("-" * 30) # Visual separator for the next loop iteration
    print("\n")
