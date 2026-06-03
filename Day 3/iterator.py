#iterator object
"""
try:
    l = [10, 20, 30]
    iterator = iter(l)
except:
    print("list not iteratable")
else:
    print("list is an iterable object")
"""
"""
try:
    t = ("Hong kong", 22, 79.7)
    iterator = iter(t)
except TypeError:
    print("tuple is not an iterable object")
else:
    print("tuple is an iterable object")
"""


#check important
scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

print(scores)
num = len(scores) // 3
print("The total number students is ", num)

total = 0

it = iter(scores)

for _ in range(num):
    s1 = next(it)
    s2 = next(it)
    s3 = next(it)

    if 0 not in (s1,s2, s3):
        total +=1

print("total students: ", total)

    