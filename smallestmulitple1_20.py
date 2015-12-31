import sys, os
truth = 0
number = 2520
check = 0

while truth == 0:
        number = number + 20
        for i in range(11,21):
                if number%i == 0:
                        check = check + 1
                else:
                        check = 0
                        break
        if check == 10:
                truth = 1	
print number
