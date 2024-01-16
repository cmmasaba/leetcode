def fibonacci(num: int):
    """
    fibonacci: computes the nth fibonacci number
    @param num: the nth number to compute the fibonacci of
    
    Returns:
        an integer
    """
    a, b, c = 0, 1, 0
    future = 0
    while c <= num - 2:
       future = a + b
       a = b
       b = future
       c += 1
    yield future

for num in fibonacci(10000):
    print(num)