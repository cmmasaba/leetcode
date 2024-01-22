def fibonacci(num: int):
    """
    fibonacci: computes the nth fibonacci number
    @param num: the nth number to compute the fibonacci of
    
    Returns:
        an integer
    """
    a, b, c = 0, 1, 0
    while c <= num - 2:
       a, b = b, a + b
       c += 1
    yield b

#for num in fibonacci(10):
#    print(num)
print(fibonacci(10).__next__())