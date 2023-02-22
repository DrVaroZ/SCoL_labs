import sys
import utilities

try:
    num1 = int(input("Enter the first integer number: "))
    num2 = int(input("Enter the second integer number: "))
    operation = input("Enter add/sub/mul/div: ")
except ValueError:
    print("Incorrect number input")
    sys.exit()

try:
    result = utilities.calculate(num1, num2, operation)
    print(result)
except ZeroDivisionError:
    print("Error, division by zero")
