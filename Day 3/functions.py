"""
arbitrary args passing
def greet (*names):
    for name in names:
        print ("Hello", name, "!")

greet ("A", "B", "C")
greet("James", "Thomas")
"""

"""
def print_star(n=1):
    for _ in range (n):
        print("************")

print_star()
print_star(2)
"""

"""
def div(a,b = 2):
    return a/b
print("div(4)=", div(4))
print("div(6,3)=", div(6,3))
"""

"""
def div(a=1, b=2):
    return a/b
print(div())
print(div(4))
print(div(6,3))"""

"""
def get_root(a,b,c):
    r1=(-b + (b**2-4*a*c) ** 0.5) / (2*a)
    r2 = (-b - (b**2-4*a*c)**0.5) / (2*a)
    return r1, r2

print(get_root(1,2,3))
"""

"""
def get_sum(a,b):
    result = a+b
    return result

sum = get_sum(3, 4)
print(sum)
sum2 = get_sum(5, 6)
print(sum2)
"""

"""
def my_greet():
         print("Welcome")

my_greet()
my_greet()
"""

"""
def max(m,n):
        if m>n:
                max = m
                min = n
                print(m, "is greater than", n)
                print(n, "is smaller than", m)
        else:
                max = n
                min = m
                print(n, "is greater than", m)
                print (m, "is smaller than", n)

max(200, 100)
"""
"""
def mile2km(mi):
    for i in range(1, mi + 1):
        miles = i * 1.61
        print(i, "km in miles is", miles, "miles")

miles = int(input("Enter km= "))
mile2km(miles)
"""
"""
def print_sum():
    a = 100
    b = 200
    result = a + b
    print("print_sum() inside: the sum of", a, "and", b, "is", result)

a = 10 
b = 20
print_sum()
"""   

print("I like {} and{}".format("Python", "Java"))



















