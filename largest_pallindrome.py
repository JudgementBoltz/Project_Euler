#This program finds the largest pallindrome
#created from the product of two three-digit numbers
import sys, os

pallindrome = 0

#find all products of two three-digit numbers
for i in range(100,1000):
    for j in range(100,1000):
        test = i*j

        #find if this number is a pallindrome
        test = str(test)
        reverse_test = test[::-1]
        test = int(test)
        reverse_test = int(reverse_test)

        if test == reverse_test:
            if test > pallindrome:
                pallindrome = test
print pallindrome
