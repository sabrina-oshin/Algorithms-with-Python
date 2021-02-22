# algorithm 01
# Complete the function solveMeFirst to compute the sum of two integers
# Contraints: 1 <= a, b <= 1000
# The code starts here:

# Initialization
a = int (input("a = "))
b = int (input("b = "))
sum_out = 0

# Defining a function
def solveMeFirst ():
  if a and b >=  1 and a and b <= 1000:
     sum_out = a+b
  else:
       return 0
  print (sum_out)

# Calling the function
solveMeFirst ()



