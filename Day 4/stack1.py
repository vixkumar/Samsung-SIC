"""
stack implementation: 

stack=[]

def push (stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

print(stack)

push(stack, "A")
print(stack)
pop(stack)
print(stack)
push(stack, "B")
print(stack)
pop(stack)
print(stack)
"""

"""
class Stack:
     def __init__(self):


def check_paranthesis(expr):
    opening = ["<html>", "<h1>", "<body>"]
    closing = ["</html>", "</body>", "</h1>"]
    stack = Stack()

    for char in expr:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if opening.index(stack.pop()) != closing.index(char):
                return False
    return stack.is_empty()

expr = input("Input a string of paranthesis: ")
print("Valid" if check_paranthesis(expr) else "Invalid")

"""


