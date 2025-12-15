# palindrome
'''def palindrome(x):
    if x==x[::-1]:
        return x
s = palindrome("MOM")
if s==s:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    '''
#factorial

'''def fact(x):
    if x==0:
        return 1
    return x * (fact(x-1))
result = fact(5)
print(result)
'''
'''def fact(x):
    f =1
    for i in range(1, x+1):
        f = f * i
    return f
result = fact(6)
print(result)
'''
#prime number
'''
num = 10
count =0 
for i in range(2, num):
    if num % i ==0:
        count =count+i
if count ==0:
    print("it is a prime number")
else:
    print("it is not a prime")
    '''
# reverse a string and number
'''str ="sudheer"
str1 =""
for i in str:
    str1 = i+str1
print(str1)
'''
'''num = 12345
reverse_num =0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 +digit
    num = num //10
print("reverse_num:",reverse_num)
'''

'''num = 1234
s = str(num)[::-1]
print(s)
'''
# fibanocci series
'''def fib(n):
    if n ==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
x = fib(10)
print(x)
'''
'''a =0
b =1 
for i in range(1,10+1):
    c = a +b
    a=b
    b=c
    print(c,'')
    '''
# Amstrong number
'''num = 123
temp = num
b = len(str(num))
count =0
while temp > 0:
    digit = temp % 10
    count = count + digit ** b
    temp = temp // 10
if count == temp:
    print("It is a Amstrong ")
else:
    print("it is not a amstrong number")
    '''
#anagram
'''num1 = "heart"
num2 = "eah"

if len(num1) == len(num2):
    if sorted(num1) == sorted (num2):
        print("it is a anagram")
    else:
        print("it is not a anagram")
else:
    print("it is not a anagaram")
    '''
#peranthasis
'''def peranthasis(para ):
    stack = []
    for c in para:
        if c in ['(','{','[']:
            return False
        stack.append()
        if not stack:
            return False
        current_char = stack.pop()
        if current_char == '(':
            if c != ')':
                return False
        if current_char == '{':
            if c != '}':
                return False
        if current_char == '[':
            if c != ']':
                return False
    if stack:
        return False
    else:
        return True
    
b=peranthasis("[()}[]")
print(b)'''

# leap year

'''def checkleap(x):
    return ((x % 4==0) and (x % 100==0) or (x% 400)==0)
y = checkleap(2005)
if checkleap == 0:
    print("it is a leapyear")
else:
    print("it is a not a leapyear")
    '''
#hcf or gcd 
'''def checkhcf(x,y):
    smallest =0
    if x > y:
        smallest =x
    else:
        smallest =y
    hcf =0
    for i in range(1, smallest+1):
        if (x % i==0) and (y % i==0):
            hcf = i
    return hcf
num1 = 12
num2 =14
print("here is 2 number {} and {} is {}".format(num1,num2,checkhcf(num1,num2)))
'''
# samllest integer

'''list =[1,0,2,3,4,5]
print(min(list))
'''

'''list=[1,2,6,4,5]
list.sort()
print(list[-1])
print(list[0])
'''

#second largest number

'''list=[1,2,3,4,546,54,66,7]
list.sort()
print(list[-2])
'''

'''list=[1,2,3,4,546,54,66,7]
list.sort()
if len(list) >= 2:
    s=list[-2]
    print("It is the second largest number",s)
else:
    print("It is not alrgest number")
    '''
# count vowels
'''def checkvowels(x):
    vowels ="aeiouAEIOU"
    count =0
    for c in x:
        if c in vowels:
            count = count + 1
        return count
i = checkvowels("sudheer")
print(i)
'''
# missing numbers

list = [1,2,3,5]
s=len(list)
total = s * (s+1)//2
res = sum(list)-total
print(res)
        



