import json


# This class represent a stack
class Stack:

    def __init__(self):
        self.stack = []

    # This function returns the top element on the stack without removing it
    def pick(self):
        return self.stack[0]

    # This function returns the top element in the stack and removes it
    def pop(self):
        return self.stack.pop(0)

    # This function insert new element to the top of the stack
    def push(self, value):
        self.stack.insert(0, value)

    # This function returns all the data of the stack in string
    def __str__(self):
        return "\n".join(str(val) for val in self.stack)

    # This function returns all the stack elements
    def get_all_stack_elements(self):
        temp_s = Stack()
        values = []

        for i in range(len(self.stack)):
            values.append(self.pick())
            temp_s.push(self.pop())

        for i in range(len(temp_s.stack)):
            self.push((temp_s.pop()))

        return values

    # This function returns the length of the stack
    def stack_len(self):
        return len(self.stack)
