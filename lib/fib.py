def recursive_fibonacci(n):
    """Return the n'th number of the fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
