import sys,os

def even_fib_sum():
    limit = int(raw_input("Upper Limit: "))
    x = 1
    y = 2
    i = 0
    g = 0
    sum = 2
    
    while (i < limit):
        g = g + 1
        if i%2 ==0:
            sum = sum + i
        i = x + y
        x = y + 0 
        y = i + 0

    return sum

sol = even_fib_sum()

print sol
