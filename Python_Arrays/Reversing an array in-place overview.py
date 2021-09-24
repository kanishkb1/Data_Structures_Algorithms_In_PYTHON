#Interview Question #1

#The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

#For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

#Using indexing and slicing
T = [1,2,3,4,5]
print(T[::-1])


#Design algorithm
#For a given array, we will take two index terms, startIndex and endIndex.
#We will increment startIndex and decrement endIndex until they meet at same value.
def reverse(nums):
    #Declaration of indexes
    start_index = 0
    end_index = len(nums) -1

#Swapping of indexes
    while end_index > start_index:
        nums[start_index],nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index +1
        end_index = end_index -1

#Main function
if __name__ == '__main__':
    n=[1,2,3,4,5]
    reverse(n)
print(n)