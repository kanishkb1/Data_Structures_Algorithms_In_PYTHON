#Interview Question #2

#"A palindrome is a string that reads the same forward and backward"

#For example: radar or madam

#Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! 


d='madam'
if d == d[::-1]:
    print ("Palindrome exists")
else:
    print("Palindrome not exist!")


def is_palindrome(s):
    orignal_string =s
    reversed_string = reverse(s)
    if orignal_string ==reversed_string:
        return True
    else:
        return False    


def reverse(data):
    #pointing to the first item
    start_index = 0
    #pointing to the last item
    end_index =len(data)-1

    while end_index > start_index:
        data=list(data)
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index =start_index +1
        end_index=end_index-1
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('madam'))