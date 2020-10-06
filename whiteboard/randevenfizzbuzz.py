""" Prompt: Given a random number as an input to a function, 
    return "FIZZ" if the number is even
    and "BUZZ" if the number is odd
"""
import random

def fizzbuzz(number):
    if number % 2 == 0:
        return "FIZZ"
    return "BUZZ"

val_rand = random.randint(0, 100000)
print(f"The random number is {val_rand} and that's a {fizzbuzz(val_rand)}!")

