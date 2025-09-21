"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

import math

def is_factor(d, n):
     return d != 0 and n % d == 0

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if is_factor(2, n):
        return False
    limit = math.isqrt(n)
    for d in range(3, limit + 1, 2):
        if is_factor(d, n):
            return False
    return True

list_of_primes = [n for n in range(2, 10001) if is_prime(n)]
print(list_of_primes)
