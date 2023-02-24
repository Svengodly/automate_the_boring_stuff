import logging
import random


def binary_search(array, answer, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1
    guess = (low + high) // 2
    if guess == array.index(answer):
        return print(f"Correct! The answer was {answer}")
    elif guess > array.index(answer):
        print(f"Lower than {array[guess]}")
        high = guess - 1
        binary_search(array, answer, low, high)
    else:
        print(f"Higher {array[guess]}")
        low = guess + 1
        binary_search(array, answer, low, high)


numbers = []

for value in range(1, 10000):
    numbers.append(value)

chosen = random.choice(numbers)

binary_search(numbers, chosen)

