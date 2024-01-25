def odd_product(array: list) -> list:
    """
    odd_product - find all distinct pairs of numbers whose product is odd
    :param array: list of length n
    :return: list of all distinct pair of  numbers whose product is odd
    """
    return [(array[i], array[j]) for i in range(len(array)) for j in range(i + 1, len(array)) if (array[i] * array[j]) % 2 == 1]

def main():

    array = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    print(odd_product(array))

if __name__ == "__main__":
    main()