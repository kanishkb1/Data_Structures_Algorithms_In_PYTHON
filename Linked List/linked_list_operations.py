#Linked List operations

class Node:
    def __init__(self,data):
        self.data =data
        self.nextNode=None

class LinkedList:
    def __init__(self):
        self.head =None
        self.numOfNodes =0

    def insert_start(self,data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self,data):
        self.numOfNodes = self.numOfNodes + 1
        new_node =Node(data)

        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        actual_node.nextNode = new_node

    def size_of_linked_list(self):
        return self.numOfNodes
    

    def remove(self,data):
        if self.head is None:
            return 

        actual_node = self.head
        previous_node =None
        while actual_node is not None and actual_node.data!=data:
            previous_node =actual_node
            actual_node=actual_node.nextNode

        if actual_node is None:
            return

        if previous_node is None:
            self.head=actual_node.nextNode

    def transverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode


    

