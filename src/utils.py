def add(*args: float | int) -> float:
    """Return the sum of all numbers."""
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    return sum(args)


def subtract(*args: float | int) -> float:
    """Subtract all following numbers from the first."""
    if not args:
        return 0
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
