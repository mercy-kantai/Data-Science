
# #   Implementing stacks using lists
stack = []

stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')


print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
print(type(stack))

#Implementing stacks using deque
from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('e')



# LIFO order

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
print(type(stack))






class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

   
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Pop items from the stack and print the popped items
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)
print(type(stack))


# Method Two
# Program to implement a stack using
# two queue
from collections import deque
class Stack:
    def __init__(self):
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        self.q1.append(x)
    def pop(self):
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
    def top(self):
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())
        # Pop the only left element from q1 to q2
        top = self.q1[0]
        self.q2.append(self.q1.popleft())
        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
        return top
    def size(self):
        return len(self.q1)

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print( s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    print(s.size())



