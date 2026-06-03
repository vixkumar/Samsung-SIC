"""
#sum of n numbers
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
m= int(input("Enter a number: "))
print(sum(m))
"""

def power(x,n):
    if n == 0:
        return 1
    else:
       return x * power(x, n-1)
    
x = int(input("Enter x: "))
n = int(input("Enter n: "))
print(power(x,n))
