
# Asking user for numbers and operator
num1 = float(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

# Operators
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "^":
    print(num1 ** num2)
else:
    print("Error: Invalid operator")
