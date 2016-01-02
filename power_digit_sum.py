x = long(2**1000)
x = str(x)

summation = 0
#a string is an iterable
for i in x:
    summation = summation + int(i)
    
print summation