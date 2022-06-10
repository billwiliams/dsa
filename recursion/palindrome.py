# Recusively check if a string is a palindrome

def is_palindrome(string):

    #Base Case
    if len(string)==0 or len(string)==1:
        return True
    else:
        if string[0]!=string[-1]:
            return False
        return is_palindrome(string[1:-1])


print(is_palindrome("a"))
print(is_palindrome("aba"))
print(is_palindrome("abc"))
print(is_palindrome("baab"))