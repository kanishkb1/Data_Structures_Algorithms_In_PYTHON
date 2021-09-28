#Construct an algorithm to check whether two words (or phrases) are anagrams or not!

#"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"

#For example: restful and fluster

def is_anagram(str1,str2):
    #if the length differ, then it is not anagram
    if len(str1) != len(str2):
        return False
    
    #we have to sort the letters of the string and then wehave to compare same indexes
    str1 = sorted(str1)
    str2=sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == '__main__':
    s1 = ['f','l','u','s','t','e','r']
    s2=  ['r','e','s','t','f','u','l']
    print (is_anagram(s1,s2))
