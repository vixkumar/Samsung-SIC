"""
ages = [34, 39, 17, 48, 67]
print("Adult: ")
for a in filter(lambda x:x>=19, ages):
    print (a)
"""

"""
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in filter(lambda x:x%2 == 0, n_list): # here filter is used
    print(i)
"""

"""
lower = ["a", "b", "c", "d"]

upper = list(map(lambda x:x.upper(), lower)) # here map is used 
print("upper_a_list: ", (upper))
"""

from functools import reduce

n = int(input("Enter range: "))
sum = reduce(lambda x, y: x+y, range(1, n+1))
print("Sum of 1 to 100: ", sum)


   
