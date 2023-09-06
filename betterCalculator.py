# This calculator can perform all basic arithmetic (add, sub, multiply, & divide)
#   The user can also select which operation to perform

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, or /): ")

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print("Invalid operator")
