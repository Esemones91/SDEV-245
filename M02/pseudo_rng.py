"""
    Filename: pseudo_rng.py
    Author: Erick Semones
    Asgnmnt: M02 Find the Security Flaw
    Date: 01/23/2025

    This script produces 100 pseudo-random
    number between 0 and 100.
    """


import random

random_numbers: list = []

for i in range(100):
    random_numbers.append(random.randint(0, 100))
print(random_numbers)
