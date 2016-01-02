#Since moving from the top left corner to the bottom right
#corner of a 20x20 lattice requires 20 right moves and
#20 down moves, we can solve this problem by thinking of it
#as a completely different problem. Consider a deck of 40 cards
#where 20 say "right" on them and 20 say "down", an identical problem
#would be, "How many unique arrangements of these cards are there?"
#To solve this we use the simple equation for N total objects with
#A repeated objects and B repeated objects, N!/(A!*B!)

from math import factorial
A = B = 20
N=40

solution = factorial(N)/(factorial(A)*factorial(B))
print solution
