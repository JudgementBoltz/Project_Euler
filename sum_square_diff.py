import sys, os

squared_sum  = 0
sum_of_squares = 0

for i in range(1,101):
        squared_sum = squared_sum + i
        sum_of_squares = sum_of_squares + i**2

solution = -1*sum_of_squares + (squared_sum**2)
print solution
