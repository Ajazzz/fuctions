def factorial(n):
    """
    Calculate the factorial of a number n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

    
n=5
print(factorial(n))
#OUTPUT = 120
