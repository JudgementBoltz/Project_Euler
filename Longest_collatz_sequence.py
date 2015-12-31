import sys, os

length = 0
answer = 0

for i in range(500000,1000000):
	count = 0
	n = i
	while n != 1:
		if n%2 ==0:
			n = n/2
		else:
			n = (3*n + 1)/2
			count = count+1
		count = count + 1
		
	if count > length:
		length = count
		answer = i
		
		
print answer
