 ''' Function to calculate the factorial of a number:

def factorial(n):
    """
    Calculate the factorial of a number n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
