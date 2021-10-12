#FIFO Structure- First item we insert is the first one we take out\

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    #this operation has O(1) complexity
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue (self):
        data =self.dequeue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)       
print('Size: %d' % queue.size_queue())