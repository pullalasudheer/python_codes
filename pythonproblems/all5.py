#fibanocc series

'''a = 0
b = 1
for i in range(10-1) :
    c = a+b
    print(c)
    a = b
    b = c
'''
'''def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (fib(x-1)+fib(x-2))
print(fib(10))
'''

#palindrome

'''def palindrome(x):
    if x==x[::-1]:
        print(" it is palindrome")
    else:
        print("it is nor a palindrome")
print(palindrome("mom"))
'''

#factorial

'''def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
print(fact(5))
'''

'''def fact(x):
    f = 1
    for i in range(1,x+1):
        f=f * i
    return f
print(fact(10))
'''

#prime

'''num = 10
count = 0
for i in range(2,num+1):
    if i % num ==0:
        count = count + i
if count == num:
    print("it is a prime")
else:
    print("it is not a prime")
    '''
 # amstrong num

'''num  = 153
b = len(str(num))
temp = num
count = 0
while temp > 0:
    digit = temp % 10
    count = count + digit ** b
    temp = temp // 2
if temp == count:
    print(" it is a amstrong number")
else:
    print(" it is not a amstrong number")
'''

num = input()
b = len(str(num))
sum = 0 
for i in num:
    sum = sum + int(i) ** b
if num == sum:
    print(" it is a amstrong number")
else:
    print(" it is not a amstrong num")
    


