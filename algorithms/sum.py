def add(num: int) -> int:
    """
    sum - find the sum of the squares of all positive integers
    less than num
    @param num: find the sum of squares of +ve integers less than num
    """
    squares_sum = sum((i * i for i in range(num)))
    return squares_sum

print(add(5))