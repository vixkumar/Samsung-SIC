#refer fist class functions
def plus (a,b):
    return a + b
def minus (a, b):
    return a-b

list1 = [plus, minus]
a = list1[0](100, 200)
b = list1[1](100, 200)
print(a)
print(b)

def a():
    print("A")
def b():
    print("B")
    return(a)
b()

