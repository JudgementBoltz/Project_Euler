import sys, os

def largest_prime_factor():
    n = int(raw_input("Enter a number: "))

    #remove factors of 2
    while n%2 == 0:
        n = n/2

    #remove factors of 3 then odd factors
    x = 3
    while n > 1:
        while n%x == 0:
            factor = n
            n = n/x
        x = x+2

    return factor

print largest_prime_factor()
        
