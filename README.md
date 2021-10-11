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
      
      
