import sys, os
n  = 1000
product = 1

def pythagorean_triple(n):
        for a in range(1,500):
                for b in range(2,501):
                        c = (a**2 + b**2)**(0.5)
                        if c%1==0 and (a+b+c)==n:
                        	return [a,b,c]

sides = pythagorean_triple(n)

for i in sides:
        product = product*i
print product
			

			
