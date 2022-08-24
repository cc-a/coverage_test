from lib.fib import recursive_fibonacci, another_function


def test_fib():
    assert recursive_fibonacci(1) == 1

def test_fib2():
    assert recursive_fibonacci(5) == 5

def test_another_function():
    another_function()
