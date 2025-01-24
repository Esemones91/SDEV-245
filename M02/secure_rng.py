"""
    Filename: secure_rng.py
    Author: Erick Semones
    Asgnmnt: M02 Find the Security Flaw
    DAte: 01/24/2025

    This script produces 100 random numbers
    between 0 and 100.
    """


import sys
import random

secure_numbers: list = []
csprng = random.SystemRandom()

for i in range(100):
    secure_numbers.append(csprng.randint(0, 100))
print(secure_numbers)
