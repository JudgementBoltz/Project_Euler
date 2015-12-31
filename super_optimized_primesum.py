import sys, os

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for index,value in enumerate(primes):
        if value is True and index > n ** 0.5 + 1:
            sum += index
        elif value is True:
            primes[index*2::index] = [False] * (((n - 1)//index) - 1)
            sum += index
    return sum


print prime_sum(2000000) 
