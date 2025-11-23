# Simple Calculator Program
print("Welcome to Basic Calculator!")
print("Operations: +, -, *, /")
# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
# Perform calculation based on operation
if operation == "+":
 result = num1 + num2
 print(f"{num1} + {num2} = {result}")
elif operation == "-":
 result = num1 - num2
 print(f"{num1} - {num2} = {result}")
elif operation == "*":
 result = num1 * num2
 print(f"{num1} * {num2} = {result}")
elif operation == "/":
 if num2 != 0:
  result = num1 / num2
  print(f"{num1} / {num2} = {result}")
 else:
   print("Error: Cannot divide by zero!")
else:
 print("Invalid operation! Please use +, -, *, or /")