#fibonocci series

'''a=0
b=1
for i in range(1,10):
    c = a+b
    a=b
    b=c
    print(c)
    '''
'''def fib(x):
    if x==1 or x==2:
        return 1
    else:
        return(fib(x-1)+ fib(x-2))
p=fib(10)
print(p)
'''

#palindrome

'''def pali(s):
    if s==s[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
c = pali("sudheer")
print(c)
'''
#factorial

'''def fact(x):
    f=1
    for i in range(1,x+1):
        f = f* i
    return f
s= fact(5)
print(s)
'''

'''def fact(x):
    if x ==0:
        return 1
    else:
        return x * fact(x-1)
c =fact(5)
print(c)
'''

# prime numbers

'''n = int(input())
count =0
for i in range(2,n):
    if n % i==0:
        count += i
if count==0:
    print("it is a prime")
else:
    print("it is not a prime")
    '''


#Amstrong number

'''num = 123
temp = num
b =len(str(num))
count = 0
while temp > 0:
    digit = temp % 10
    count = count +digit ** b
    temp = temp //10
if temp == count :
    print("it is a amstrong")
else:
    print(" it is not a amstrong number")
    '''

'''num = input()
b= len(str(num))
count =0
for i in num:
    count = count + int(i) ** b
if count == num:
    print("it is amstrong")
else:
    print("it is not an amstrong number")
    '''

#anagram

'''str1="heart"
str2="earh"

if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print(" i am anogram")
    else:
        print(" i am not a anagram")
else:
    print(" i am not a anagram")
    '''

# smallest positive number

'''n = [1,2,3,5,6]
n.sort()
print(n[0])
'''

# leap year

'''def checkleap(x):
    if ((x%4==0) and (x%100!=0) or (x%400==0)):
        print(" it is a leap year")
    else:
        print("it is not a leap year")

checkleap(2024)
'''

#hcf or gcd
'''def checkhcf(x,y):
    smallest=0
    if x> y:
        smallest = y
    else:
        smallest = x
        hcf =0
        for i in range(1, smallest+1):
            if x%i ==0 and y % i ==0:
                hcf=i
        return hcf
x = 12
y=14
        print("check the hcf to {} and {} is {}".format(x,y,checkhcf(x,y)))
'''
# reverse of  a string are  number

'''str = "sudheer"
str1 =""
for i in str:
    str1 = i + str1
print(str1)
'''

'''num = 123
reverse=0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("reverse",reverse)
'''
# largest and smallest

'''list = [1,2,3,4,5,3,1,2,4]
list.sort()
smallest= list[0]
largest= list[-1]
print("smallest:",smallest)
print("largest:", largest)
'''
# vowels

'''def checkvowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    for i in str:
        if i in vowels:
            count = count + 1
        return count
str = input()
print(checkvowels(str))
'''

#missing numbers


'''def missingnumber(arr,n):
    total_num= n * (n+1)//2
    total_arr=sum(arr)
    return total_num - total_arr
arr=[1,2,3,4,6,7]
n=7
print("Misiing number",missingnumber(arr,n))
'''

# pangram

'''num = input().strip()
arr="abcdefghijklmnopqrstuvwxyz"
if num == arr:
    print(" it is a pangram")
else:
    print(" it is no a pangram")
    '''

# remove duplicate

'''list1 = [1,2,1,2,3,4,5,5,3,2,1,1,3]
res=[]
for i in list1:
    if i not in res:
        res.append(i)
print(res)
'''

# multiplication
'''n= int(input())
m= int(input())
for i in range(m+1):
    print(str(n)+ "x" + str(i) + "=" + str(n*i))
    '''
# matrix

x =[
    [2,3],
    [4,5],
    [6,7]
]
result =[
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for k in range(len(x[0])):
        result[k][i]=x[i][k]
for j in result:
    print(j)




    









