def add(num: int) -> int:
    """
    sum - find the sum of the squares of all positive integers
    less than num
    @param num: find the sum of squares of +ve integers less than num
    """
    squares_sum = sum((i * i for i in range(num)))
    return squares_sum

def main():
    try:
        num = int(input("Enter an integger value: "))
        print(f'The sum of all positive integers less than {num} is', add(num))
    except ValueError as e:
        print("You didn't enter a number!")

main()