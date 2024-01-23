def product(array1: list, array2: list) -> list:
    """
    product - find the dot product of two arrays
    :param array1: list of length n
    :param array2: list of length n
    :return: dot product of array1 and array2
    """
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of equal length")
    return [array1[i] * array2[i] for i in range(len(array1))]

def main():
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    print(product(array1, array2))

if __name__ == "__main__":
    main()