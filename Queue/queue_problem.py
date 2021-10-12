#The aim is to design a queue abstract data type with the help of stacks.



class Queue:
    def __init__(self):
        #use one stack for enqueue operation
        self.enqueue_stack = []
        #use another stack for dequeue operation
        self.dequeue_stack = []

        #adding item to the queue
        def enqueue(self,data):
            self.enqueue_stack.append(data)

        #getting items
        def dequeue(self):
            if len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0:
                raise Exception("Stacks are empty")

            if len(self.dequeue_stack)==0:
                while len(self.enqueue_stack)!=0:
                    self.dequeue_stack.append(self.enqueue_stack.pop())


            return self.dequeue_stack.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)           
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())

    queue.enqueue(100)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())