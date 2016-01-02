def triangle_num_sum(n):
    num_sum = n*(n+1)/2
    return num_sum
    
def factors_of(num_sum):
    return set(reduce(list.__add__, ([i, num_sum/i] for i in range(1,int(num_sum**0.5)+1) if num_sum%i==0)))
    
n = 500
num_sum = triangle_num_sum(n)
num_factors = len(factors_of(num_sum))
while num_factors < 501:
    n = n + 1
    num_sum = triangle_num_sum(n)
    num_factors = len(factors_of(num_sum))
    
print num_sum