'''
def ispolidrome(s):
    return s==s[::-1]
s="sudheer" 
ans=ispolidrome(s)
if ans:
    print("It is a polindrome")
else:
    print("It is not a polindrome")
'''
def is_palindrome(s):

    return s==s[::-1]
ans=is_palindrome("sudheer")
if ans:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
