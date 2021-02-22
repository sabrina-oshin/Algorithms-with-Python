# algorithm 03 : code without importing numpy
# Complete the aVeryBigSum function and it must return the sum of all array elements
# Keep in mind that some of those integers may be quite large.
# The code starts here:

# Taking the array input
n = int (input())

# Appending the user input in the list sequentially
A = list (map(int,input().strip().split())) [:n]

# Defining the function
def aVeryBigSum ():
    sum_array = 0
    for i in range (0, n):
       sum_array = sum_array + A[i]
    print (sum_array)

# Calling the function
aVeryBigSum ()
    