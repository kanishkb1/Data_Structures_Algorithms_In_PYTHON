#LIFO structure

class Stack:
    def __init__(self):
        #1-D array
        self.stack = []

    #o(1)
    #push method
    def push(self,data):
        self.stack.append(data)

    #pop method
    #O(1)
    def pop(self,data):
        if self.stack_size() < 1:
            return
            
        data=self.stack[-1]
        del self.stack[-1]
        return data
    #it returns the last item without removing it
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []


    def stack_size(self):
        return len(self.stack)

stack=Stack()
print('Pushed Item')
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print('Size: %d'% stack.stack_size())

print('Pop item')
stack.pop(2)
stack.pop(3)
print('Size: %d'% stack.stack_size())
