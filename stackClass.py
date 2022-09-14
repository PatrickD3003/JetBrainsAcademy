class Stack:
    stack = []
    def __init__(self):
        pass

    def push(self, el):
        return self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

a = Stack()

