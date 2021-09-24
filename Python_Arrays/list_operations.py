#Python List operations

#creation of list
array = [10,3,6,7,33]
print(array)

#random accessing start with 0
print(array[0])

#accessing some of the items
print(array[0:2])

#access last item
print(array[:-1]) 

#access string and numerical data-types
array= [10.0,3,8,5,7,54,70]

#updation (insertion) in the list
array[1] = 'Kevin'
print(array)

array[1] = 21
print(array)

#Linear search 
#Time complexity- O(N)
#Search for maximum item
max= array[0]
for num in array:
    if num > max:
        max=num

print(num)

#Search for minimum item
min = array[0]
for n in array:
    if num < min:
        min=num
print(int(min))

