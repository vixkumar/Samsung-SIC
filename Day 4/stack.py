class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)


# Testing the stack
st = Stack()

print(st.is_empty())  # True

st.push(10)
st.push(20)
st.push(30)

st.display()          # [10, 20, 30]

print(st.peek())      # 30

print(st.pop())       # 30
print(st.pop())       # 20

st.display()          # [10]

print(st.size())      # 1
print(st.is_empty())  # False
    