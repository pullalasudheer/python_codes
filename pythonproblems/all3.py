# fibonacci series
'''a = 0
b = 1
for i in range(10):
    c = a+b
    a=b
    b=c
    print(c)
    '''

'''def fib(x):
    if x==1 or x == 2:
        return 1
    else:
        return(fib(x-1)+ fib(x-2))
p=fib(10)
print(p)
'''

# palindrome

'''def checkpali(x):
    if x==x[::-1]:
        print(" It is palindrome")
    else:
        print("it is not a palindrome")
checkpali("mom")
'''

#factorial number

'''def checkfact(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    return f
p = checkfact(5)
print(p)
'''

'''def checkfact(x):
    if x==0:
        return 1
    else:
        return x * checkfact(x-1)
s=checkfact(5)
print(s)
'''

#prime factor 
'''n = 1
count = 0
for i in range(2,n):
    if n % i ==0:
        count = count + i
if count ==0:
    print(" it is a prime")
else:
    print(" it is not a prime")
    '''

#amstrong number

'''n = 153
temp = n
b = len(str(n))
count = 0
while temp > 0:
    digit = temp % 10
    count = count + (digit ** b)
    temp = temp// 10
if count == temp :
    print(" it is a amstrong number")
else:
    print(" it is  not a amstrong number")
    '''

'''num = 123
b = len(str(num))
sum = 0
for i in num:
    sum = sum + int(i)**b
if sum == num:
    print( " it is a amstrong number")
else:
    print(" it is not a amstrong number")
    '''

# anagram

'''num1 = "heart"
num2= "earth"
if len(num1) == len( num2):
    if sorted(num1) == sorted(num2):
        print(" it is anagram")
    else:
        print(" it is not a anagram")
else:
    print(" it is no a anagram")
    '''



# smallest positive

'''num = [100,56,9,3489,77,5,3,677,433]
num.sort(reverse=True)
print(num[0])
'''
# leap yaer

'''def checkleap(x):
    if (((x%4==0) and (x % 100!=0)) or ( x % 400 ==0)):
        print( " it is a leap year")
    else:
        print( " it is not a leap year")
checkleap(400)
'''

# hcf or gcd
'''def checkhcf(x,y):
    smallest =0
    if x > y:
        smallest =y
    else:
        smallest = x
        hvf =0
        for i in range(1, smallest+1):
            if x % i==0 and y % i ==0:
                hcf =  i
        return hcf
x= 10
y = 50
print("hcf is to num {} and {} is {}".format(x,y,checkhcf(x,y)))
'''


# reverse of a string

'''str = "sudheer"
str1=" "
for i in str:
    str1= i +  str1
print(str1)
'''

'''num = 123456
a = str(num)[::-1]
print(a)
'''

'''num = 123343148714
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num=reverse_num * 10 + digit
    num = num // 10
print(reverse_num)
'''
# largest and smallest 

'''num = [1,2,3,4,5,7,5,4,4,6,5,4,3,2,4,5]
num.sort()

smallest = num[0]
largest = num[-1]

print(smallest)
print(largest)
'''

'''num=[1,2,3,4,5,6]

large = 0
small= num[0]
for i in num:
    if i > large:
        large = i
    elif i < small:
        small = i
print(large)
print(small)
'''
# missing number

'''num = [1,2,4,5]
b = len(num)
total = b * (b+1)//2
res= sum(num) - total
print(res)
'''
'''def missingnum(arr,n):
    total_num = n * (n+1)//2
    total_arr= sum(arr)
    return total_num - total_arr
arr = [1,2,3,5,6]
n = 6
print(missingnum(arr,n))
'''

# remove dulicate

'''num = [1,2,3,1,2,3,4,5,6,6,5,4,3,5,7,9,9,8]
res=[]
for i in num:
    if i not in res:
        res.append(i)
print(res)
'''

# pangram


'''a = input().split()
b = "abcdefghijklmnopqrstuvwxyz"
a.sort()
if a==b:
    print("True")
else:
    print("False")
    '''

# repation

'''num = [ 1,1,2,3,4,5,7,2,1,3,5,7,8,7,5,4,3,3,3,5,7,8,7,5,4]
for i in num:
    print(i,"=",num.count(i),"Times")
    '''

# mumtiplication
'''m = int(input())
n = int(input())
for i in range(n+1):
    print( str(m) + "x" +str(i) + "=" + str(m*i))
    '''


# matrix 
x =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
y = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result= [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y [j][k]
for r in result:
    print(r)
            







