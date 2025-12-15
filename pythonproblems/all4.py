# fibinooci series

'''a = 0
b = 1
for i in range(10+1):
    c = a+ b
    a = b
    b = c
print(c)
'''

'''ef fib(i):
    if i<= 1:
        return 1
    else:
        return (fib(i-1) + fib( i-2))
for i in range(10):
    print(fib(i),end=',')
    '''

# palindrome

'''def pali(x):
    if x == x[::-1]:
        print(" it is a palinfrome")
    else:
        print(" it is not a palindrome")
pali("mom")
'''
# factorial

'''def fact(x):
    f = 1
    for i in range(1,x+1):
        f = f * i
    return f
p =fact(5)
print(p)'''

'''def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
p = fact(5)
print(p)'''

# prime

'''num = 1
count = 0
for i in range(2,num+1):
    if i % num ==0:
        count += i
if count == num:
    print(" it is a prime")
else:
    print(" it is not a prime")
    '''

# amstrong number

'''num = 153
b =  len(str(num))
temp = num
count =0
while temp > 0:
    digit = temp % 10
    count += digit ** b
    temp = temp // 2
if num == temp:
    print(" it is a amstrong number")
else:
    print(" it is not a amstrong number")
    '''

'''num = 123
b = len(str(num))
sum = 0
for i in range(num):
    sum = sum + len(i) ** b
    '''

# Anagram

'''num1 ="heart"
num2 ="eah"

if len(num1) == len(num2):
    if sorted(num1) == sorted(num2):
        print(" it is a anagram")
    else:
        print(" it is not a anagram")

else:
    print(" it is not a anagram")
    '''

# smallest num

'''num = [1,2,3,7,5,6,8,6]
num.sort()
print(num[-1])
'''

# leap year
'''def leap(x):
    if (x% 4==0 and x % 100!=0) or x % 400 == 0:
        print(" it is a leap year")
    else:
        print(" it is not a leap year")
a= leap(400)
print(a)
'''
#hcf

'''def checkhcf(x,y):
    smallest =0
    if x> y:
        smallest = y
    else:
        smallest = x
        hcf=0
        for i in range( 1, smallest+1):
            if x % i ==0 and y % i ==0:
                hcf = i
        return hcf
x = 12
y = 14
print(" id the hcf 2 divide {} and {}  is {}".format(x,y,checkhcf(x,y)))

'''

# reverse a string

'''str = "sudheer"
str1 = ""
for i in str:
    str1 += i
print(str1)
'''
'''tr1 = 1234455
b=len(str(str1))
sum =0
while str1 > 0:
    digit = str1 % 10
    sum = sum * 10 + digit
    str1= str1//10
print(sum)
'''
# missing numbers
'''def missing(arr,n):
    total_num= n * (n+1)//2
    total_arr= sum(arr)
    return total_num - total_arr
arr = [ 1,2,3,5,6]
n = 6
print(missing(arr,n))
'''

# remove dulicate

'''num= [1,2,3,3,2,1,3,4,6,6,3,2,2,4,6,3]
res = []
for i in num:
    if i not in res:
        res.append(i)
print(res)
'''
# pangram

'''a = input().split()
b = 'abcdefghijklmnopqrstuvwxyz'
a.sort()
if a==b:
    print(" it is pangram")
else:
    print(" it is not a pangram")
    '''

# repitation
num = [1,1,1,1,2,3,2,2,2,2,3,34,4,5,5,5,5,5,4,4,4,4,4,6,6,7,7,7,7,7,7,6,4,3,3,4,5,7,8,8,8,8,8]
for i in num:
    print(i,'=',num.count(i),'times')




    

    




