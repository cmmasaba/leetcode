def fibonacci(n: int) -> int:
    """
    fibonacci: computes the nth fibonacci number
    @param n: the nth number to compute the fibonacci of
    
    Returns:
        an integer
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print(fibonacci(6))

main()