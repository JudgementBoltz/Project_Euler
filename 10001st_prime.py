import sys, os
count = 2
i = 3
primes = [2,3]

while len(primes) != 10001:
        is_prime = 0
        i = i + 2
        for x in primes:
                if i%x == 0:
                        break
                else:
                        is_prime = is_prime + 1
                        
        if is_prime == len(primes):
                primes.append(i)

print i
