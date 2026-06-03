"""
n = int(input("Enter sum of n numbers: "))
sum = 0
for i in range (1, n+1) :
    sum += i

print (sum)
"""

n = int(input("Enter sum of n even numbers: "))
sum = 0 
for i in range (1, n+1, 1) :
    if (i % 2) == 0 :
        sum += i
    else :
        i+1

print ("sum =", sum)



