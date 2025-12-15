'''def is_palindrome(x):
    return x==x[::-1]
ans = is_palindrome("sudheer")
if ans:
    print("it is palindrome")
else:
    print("it is not palindrome")
'''
'''def fib(s):
    if s==1 or s==2:
        return 1
    else:
        return(fib(s-1)+fib(s-2))
x=fib(10)
print(x)
'''
'''a =0
b = 1
for i in range(10):
    c = a+b
    a=b
    b=c
    print(c,end="  ")
    '''
'''def fac(s):
    f=1
    for i in range(1,s+1):
        f = f * i
    return f
x= fac(5)
print(x)
'''
'''def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)
x =fac(5)
print(x)
'''
num = 1000
count=0
for i in range(2,num):
    if num % i==0:
        count+=1
if count==0:
    print("prime")
else:
    print("not prime")

