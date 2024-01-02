def solution(lengthA, lengthB) -> int:
    max_size = 0
    max_size = max(max_size, lengthB//4)

    if lengthA >= lengthB//3:
        max_size = max(max_size, lengthB//3)
    else:
        max_size = max(max_size, lengthA//1)
    
    if lengthA >= 2*(lengthB//2):
        max_size = max(max_size, lengthB//2)
    else:
        max_size = max(max_size, lengthA//2)

    if lengthB >= lengthA//3:
        max_size = max(max_size, lengthA//3)
    else:
        max_size = max(max_size, lengthB//1)
    
    max_size = max(max_size, lengthA//4)
    return max_size

def main():
    lengths = [[13, 11], [10, 21], [2, 1], [1, 8]]
    for item in lengths:
        print(solution(*item))
    
if __name__ == '__main__':
    main()