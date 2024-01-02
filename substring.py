def soluton(message: str):
    substrings = []
    for letter in message:
        if substrings:
            if letter in substrings[-1]:
                substrings.append(letter)
            else:
                substrings[-1] += letter
        else:
            substrings.append(letter)
    return len(substrings)

def main():
    words = ['cycle', 'apple', 'world', 'abba']
    for word in words:
        print(soluton(word))

if __name__ == '__main__':
    main()