from typing import Union


def add(*args: Union[float, int]) -> float:
    """Return the sum of all numbers."""
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    print("Zero errors detected the sum will happen")
    return sum(args)


def subtract(*args: Union[float, int]) -> float:
    if not args:
        return 0
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args: Union[float, int]) -> float:
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args: Union[float, int]) -> float:
    if not args:
        return 0
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Division by zero is not allowed.")
        result /= num
    return result
