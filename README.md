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
