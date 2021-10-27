# Data_Structures_Algorithms_In_PYTHON
This repository contains all the data structures and algorithms in Python language.

## Data Structures
->Data Structures came to be in order to manage large amounts of data efficiently.
-> how to deal with huge amounts of data?
-> Somehow we have to make sure that the application is fast as possible and that is exactly crucial.

"Bad programmers worry about the code. Good programmers worry about data structures and their relationships."

## 1. Difference between Abstract Data types (ADT) and data structures ?

### ADT
-> Logical description for certain data-types.

-> It is like supertype in programming.

-> We just define what methods (functions) the data structure will have so we define the basic behaviour.

->Stack abstract data type: Push(), Pop() and peek() method functions.

### Data Structures

->defines the concrte implementation or actual representation of the data.

->the aim is to be able to store and retrieve data in the efficient manner.

->Example- arrays, binary trees, linked lists.

## 2. Arrays & Lists
-> The aim is to make operations as fast as possible: inserting new items or removing items from the data structure.

-> Arrays are data structures where all items are identified with an index (starting from zero)

-> List in python = arrays in C, C++, Java.

->the items of the array are located right next to each other in the main memory (RAM), hence can be accessed by the index.

->Major advantage: Accessing the items- random access is possible.

->Running time- O(1)

->memory address = array's address + index * data-size (16-byte)

->stacks, queue and dictionaries (hash-tables).

### 2-Dimensional array
->every single item (value) can be identified with 2 indexes- rowindex and columnindex.

-> index starts with 0.

-> We can store different type of items in the list.

### Array Operations

1. Adding items- We can insert new items at the end of data structure until the data structure is not full. O(1)->Running time

What if data structure becomes full?
-> Have to allocate a larger chunk of memory in the RAM (usually 2x the size of array)

->have to copy the existing items one by one to the new array.

-> because of these operations take O(N) linear running time complexity.

2. Adding numbers to arbitrary positions

-> We want to insert an item to an arbitrary position-associated with index.

3. Removing last item

-> Removing the last item of an array data structure is quite easy and fast operation. - O(1) running time

4. Removing item from arbitrary position

-> Usually we do not know the index of the item we want to remove. After removing the item we have to deal with the holes in data structure

-> Manipulating the last item (insertion or removal)
      Running time- O(1)
      
->Manipulating arbitrary item (insertion or removal)
       Running time- O(N)

### Disadvantages of Arrays/Lists

-> We have to know the number of items we want to store at compile-time: so it is not data-structure.

-> It is not dynamic.

-> Usually do not store items with different data types.

## 3. Linked Lists

-> Another data structure whose aim is to able to store items efficiently (insertion and removal operations).

->Arrays "holes" disadvantages can be covered using the linked list.

->We have the access to the first node of the linked node and other items can be accessed by this node.

-> Last node is pointing to the NULL.

->Every node stores the data itself and a reference the next node in the linked list data structure.

-> Hence, Linked lists require more memory than arrays.

->Advantage
      -> There is no holes in data structures as there is no shifting item.
      
      ->Easy data structures and easy to implement them.
      
      ->Implement more complex structure and abstract data types such as stacks and queues.
      
      ->We can insert item at the beginning of the data structure fast- O(1) running time.
      
      ->Slow operatin to insert the item at the end-O(N) running time.
      
### Linked List Operations

1. Maninpulation he first item (insertion or removal)
                  O(1) running time-this is why we like linkedi lists.
                 
2. Manipulating arbitrary item
                  O(N) running time-if we have to do several of these operations then linked lists is not the best option possible!!
                                
                 
->Linked List Disadvantages
-> need more memory because of the references

-> there is no random access 

->can not go backwards

->not predictable-running time of the application relies on what users do.
                 
                 
#Difference between algorithms and data structures.

1. Size: Since data can only be stored in contiguous blocks of memory in an array, its size cannot be altered at runtime due to the risk of overwriting other data. However, in a linked list, each node points to the next one such that data can exist at scattered (non-contiguous) addresses; this allows for a dynamic size that can change at runtime.


2. Memory allocation: For arrays at compile time and at runtime for linked lists. but, a dynamically allocated array also allocates memory at runtime.

3. Memory efficiency: For the same number of elements, linked lists use more memory as a reference to the next node is also stored along with the data. However, size flexibility in linked lists may make them use less memory overall; this is useful when there is uncertainty about size or there are large variations in the size of data elements; memory equivalent to the upper limit on the size has to be allocated (even if not all of it is being used) while using arrays, whereas linked lists can increase their sizes step-by-step proportionately to the amount of data.

4. Execution time: Any element in an array can be directly accessed with its index; however in the case of a linked list, all the previous elements must be traversed to reach any element. 

### Linked List Application
                 
Operating system uses almost all important data-streuctures.
1. Low Memory Mangement- Important in low memory management when dealing with C programmijng malloc(0 and free(0 functions.

## Double Linked Lists

-> It is slow operation to insert items at the end. - O(N) running time

-> It is another data structure so the main aim is to store items efficiently.

-> We have to access to the first node (head node) and we have access to the last nide of the linked list(tail node).

-> Every node stores the data itself and references to the next node and to previous node.

-> Double linked list need more memory than linked lists.

->Advantage
      -> there can not be any holes in the data structures.

      -> it can be transversed in both directions.
      
      -> removing a node is easier because there is pointer to the previous node as well.
     
      
->Disadvantages

      -> need more memory because of 2 references. (2 pointers)
      
      -> a bit more complicated to implement because we hjave ti handle both of the pointers
      
      ->still have not solved the main issue- How to search for arbitrary items faster than O(N) linear running time?
      
### Middle node in linked list (problem)

      The task is to find the middle node of linked list without the need for extra memory.
 
      1) Naive solution-we iterate through list and count how many elements are in total.
            Transverse the list again and node index count/2 is the middle node.
            
      2) Using two pointers
            We can use two pointers to get middle node O(N)
            
           First pointer: traverse the linked list one node at time.
           Second pointer: traverse the linked list 
### How to reverse a linked list

Task- Construct in-place algorithm to reverse a singly linked list.

1)Naive solution-We consider all nodes one by one then construct another linked list in reverse order.
            Problem: O(N) memory complexity so it not in-place.
            
2)Using pointers:
      We can achieve an in-place algorithm that has O(N) linear time complexity as well.
      
# Stacks

->Abstract data type 

-> implemented either with arrays or linked lists

->LIFO- Last In, First Out

-> Basic Operations- Pop(), Push(), Peek()

### Applications
-> Most programming languages are stack oriented.

->Graph algorithms heavily rely on stacks (DFS implemented using stack).

->Eulerian cycle in a G(V,E) graph.

### Memory Management

-> 2 main types of memory: stack memory and heap memory.

-> The stack memory is sppcial region in the RAM (random access memory)

-> this is special data type (stack) that stores the active functions and local variables as well.

-> This is how python works where to return finish execution 

-> Stack memory- small size, fast access and no fragmentation.

-> Heap memory - large size, slow access and stored objects.

# Queues

->it is an abstract data type and can be implemented using linked lists or arrays.

->FIFO structure- First In, First out.

->Basic operations- enqueue(), dequeue(), peek().

->Several applications in operating system and thread management.

## Queue applications

->threads are stored in queues

->queues are important in CPU scheduling

->graph algorithms rely heavy on queues

# Binary Search Trees

-> Array can manipulate the last item in O(1) constant running time coplexity that is quite fast.

-> Linkied List can manipulate the first item of the data structure.

-> Searching for an arbitrary item-> O(N)

-> If data structure is sorted-O(logN) logrithmic complexity.

-> this is concept of binary search.

-> Trees- A tree is a G(V,E) undirected graph in which any two vertices are connected by exactly one path or equivalently a connected acyclic undirected graph.

-> We have access to root noe exclusively all othetr nodes can be accessed via the root node.

-> Leaf nodes with no children at all.

-> We can define parent and child relationship.

## BST details

-> Every node in the tree can have ayt most 2 childten.

-> Left child is smaler than thre parent node.

-> Right child is greater than parent node.

-> We can access the root node exclusivly and all other nodes can be accessed via root node.

->Every decision can get rid of half of the data (Binary search) and this is how can achieve O(log N) running time.

-> The height of the tree is the number of edges on longest downward between the root and a leaf node.

-> Layer h, we have 2^h - 1 nodes.

-> The logarithmic O(log N) running time is valid only when the tree is balanced.

->Should keep the height of the trees at minimum. (h=log N)

->If tree is not balanced so the h=log N relation is no more valid.

->The minimum item in the binary tree is the leftmost item in the tree.

-> The maximum item in the binary tree is the rightmost item in the tree.

## Binary search trees

1. Removing a leaf node-> Basically we have to notify the parent that the child has been removed. The node will be removed by the garbage collector.

2. Removing a node with a single child- Basically we have to notify the parent that left or right child has been changed.

3. Removing a node with two children- the smallest item in the right sutree is called successor and the largest item in the left subtree is caled predecessor.

# Binary Search Tree Traversal

1. Tree Transversal means visiting every node of binary search tree exactly once in O(N) linear running time.
2. Tree traversal- 1. Pre-order, 2. In-order, 3. Post-order trasversal
3. Pre-order-> We visit the root node of the binary tree then the left subtree and finally the right subtree in recursive manner.
4. Post-order-> We visit the left subtree of the binary tree then the right subtree and finally the root node in recursive manner.
5. In-order -> We visit the left sub-tree then the root node and finally the right subtree in recursive manner.

# Running time complexity

Worst case- O(N) for space complexity, insertion, deletion and search.

Average case- Space complexity (O(N), Insertion O(log N), Deletion O(Log(N) AND SEARCH(LOG N)


Real world applications- 1. OS, 2. Game Trees 3. Machine Learning



