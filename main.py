
num1 = 0.0
num2 = 0.0
operator = "+"

# Asking user for numbers and operator
try:
    num1 = float(input("Enter a number: "))
    operator = input("Enter an operator: ")
    num2 = float(input("Enter a number: "))
except:
    print("Invalid number")

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
