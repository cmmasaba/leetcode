def permutation(string: str):
    permutations(string, '')

def permutations(string: str, prefix: str):
    if len(string) == 0:
        print(prefix)
    else:
        n = len(string)
        for i in range(n):
            rem = string[0:i] + string[i + 1] if i < n - 1 else ''
            permutations(rem, prefix + string[i])

def main():
    string = 'apple'
    permutation(string)

main()