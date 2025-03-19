import math
import pytest

def add(a,b):
    return a + b

def test_add(): #Special name! Pytest looks for functions that start with 'test_'
    assert add(2,3) == 5 #
    assert add('space', 'ship') == 'spaceship'


def fizz_buzz(integer: int):

    if integer <= 0:
        raise ValueError("Zero or negative input.")

    if integer % 3 == 0 and integer % 5 == 0:
        return 'FizzBuzz'
    elif integer % 3 == 0:
        return 'Fizz'
    elif integer % 5 == 0:
        return 'Buzz'
    else:
        return integer


def test_fizz_buzz():       # Better to have one assert per test function.
    assert fizz_buzz(3) == 'Fizz'
    assert fizz_buzz(5) == 'Buzz'
    assert fizz_buzz(15) == 'FizzBuzz'
    assert fizz_buzz(23) == 23
    with pytest.raises(ValueError, match="Zero or negative input"):
        fizz_buzz(0)

def test_fizz_buzz2():
    with pytest.raises(ValueError, match="Zero or negative input"):
        fizz_buzz(-5)
