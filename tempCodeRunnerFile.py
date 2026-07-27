################calculator program
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /, **, %, //): ")
if operator == "+":
    print(f"Add: {num1 + num2}")
elif operator == "-":
    print(f"Subtract: {num1 - num2}")
elif operator == "*":
    print(f"Multiply: {num1 * num2}")
elif operator == "/":
    print(f"Divide: {num1 / num2}")
elif operator == "**":
    print(f"Power: {num1 ** num2}")
elif operator == "%":
    print(f"Modulus: {num1 % num2}")
elif operator == "//":
    print(f"Floor Division: {num1 // num2}")