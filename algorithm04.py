# algorithm 04
# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2]
# If a[i] > b[i], then Alice is awarded 1 point
# If a[i] < b[i], then Bob is awarded 1 point
# If a[i] = b[i], then neither person receives a point, comparison points is the total points a person earned
# Constraints  1 <= a[i] <=100, 1 <= b[i] <=100
# The code starts here:

n = 3
sum1 = 0
sum2 = 0
person1 = list ()
person2 = list ()

# Appending the user input in the list sequentially
a = list (map(int,input().strip().split())) [:n]
b = list (map(int,input().strip().split())) [:n]

# Loop to create the comparison
for i in range (0,n):
    if a[i] > b [i]:
        person1.append (1)
        person2.append (0)
    elif a[i] < b [i]:
        person1.append (0)
        person2.append (1)
    else:
        person1.append (0)
        person2.append (0)

# Summing the individual score
    sum1 = sum1 + person1[i]
    sum2 = sum2 + person2[i]

# Printing the result
print (sum1, sum2)