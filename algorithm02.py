# algorithm 02
# Complete the simpleArraySum function and it must return the sum of the array elements as an integer
# The code starts here:

import numpy as np

# Taking the array input
n = int (input())

# Appending the user input in the list sequentially
A = list (map(int,input().strip().split())) [:n]

# Defining the function
def simpleArraySum ():
    for i in range (0, n):
       sum_array = np.sum (A)
    print (sum_array)

# Calling the function
simpleArraySum ()
    
