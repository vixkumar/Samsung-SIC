"""
def greeting():
    def say_hi():
        print("Hello")
    say_hi()
greeting()
"""

"""
#refer this... function returning function:so how to handle such codes
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

f = calc()
print(f(14))
"""


