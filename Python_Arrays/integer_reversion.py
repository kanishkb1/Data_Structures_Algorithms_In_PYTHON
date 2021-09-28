#Interview Question #3

#Our task is to design an efficient algorithm to reverse a given integer. For example if the input of the algorithm is 1234 then the output should be 4321
#Using string operations
'''i=1234
i=str(i)
print(i[::-1])'''

def reverse_integer(n):
    rev =0
    rem = 0

    while n >0:
        rem = n % 10
        rev = rev *10 + rem
        n = n//10
    return rev

if __name__ == '__main__':
    print(reverse_integer(98002))