#Max in a stack problem overview
#The aim is to design an algorithm that can return the maximum item of a stack in O(1) running time complexity. We can use O(N) extra memory!

#Hint: we can use another stack to track the max item!

class MaxStack:
    def __init__(self):
        #one stack for enqueue operation
        self.main_stack = []
        #other stack for dequeue operation
        self.max_stack = []

#adding an item into queue is O(1) `
    def push (self,data):
        #pushnext item to stack
        self.main_stack.append(data)
        #first item is same in both stack
        if (len(self.main_stack)==1):
            self.max_stack.append(data)
            return

#if the item is largest one so far: we insert it onto the stack
#stack[-] is the peek operation

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    #getting items
    def pop(self):
        self.max_stack(pop)
        return self.main_stack.pop()

     
    #max item is the last item we have inserted into mazStack O(1)
    def get_max_item(self): 
        return self.max_stack.pop()

if __name__ == "__main__":
    max_stack = MaxStack()
    max_stack.push(1000)
    max_stack.push(100)
    max_stack.push(10)
    max_stack.push(1)
    print(max_stack.get_max_item())
