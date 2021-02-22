# algorithm 02 : code without importing numpy
# Complete the simpleArraySum function and it must return the sum of the array elements as an integer
# The code starts here:

# Taking the array input
n = int (input())

# Appending the user input in the list sequentially
A = list (map(int,input().strip().split())) [:n]

# Defining the function
def simpleArraySum ():
    sum_array = 0
    for i in range (0, n):
       sum_array = sum_array + A[i]
    print (sum_array)

# Calling the function
simpleArraySum ()
    