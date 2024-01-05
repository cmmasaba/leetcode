def reverse(array: list) -> list:
    for i in range(len(array)//2):
        other = len(array) - i - 1 # index for the value being swapped
        array[i], array[other] = array[other], array[i] # swap elements

    return array

def main():
    array = [1, 2, 3, 4, 5]
    print(reverse(array))

if __name__ == '__main__':
    main()