import sys
import constants


def calculate(number1: int, number2: int, operation: str) -> float:
    if operation == constants.ADD:
        return number1 + number2
    elif operation == constants.SUB:
        return number1 - number2
    elif operation == constants.MUL:
        return number1 * number2
    elif operation == constants.DIV:
        return number1 / number2
    else:
        sys.exit("Error, wrong operation")
