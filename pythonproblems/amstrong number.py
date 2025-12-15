'''n=int(input("Enter the number:"))
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+ (r**b)
    n=n//10
if s==sum1:
    print("Amstrong number")
else:
    print("not a astrong number")
    '''
'''
num = int(input("Enter the number:"))
temp = num
b = len(str(num))
sum =0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** b
    temp = temp//10
if sum == temp:
    print(" it is amstrong number")
else:
    print("it is not an amstrong number")
    '''
'''num = input("Enter the number:")
b = len(str(num))
sum =0
for i in num:
    sum = sum + int(i)**b
if sum == num:
    print(" i am strong number")
else:
    print("i am nit amstrong")
    '''

num = 153
temp = num
b = len(str(num))

count = 0
while temp > 0:
    digit = temp % 10
    count = count + (digit ** b)
    temp = temp // 10
if temp == count:
    print(" it is a amstrong number")
else:
    print(" it is not amstrong number")

n=int(input("Enter the number:"))
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+ (r**b)
    n=n//10
if s==sum1:
    print("Amstrong number")
else:
    print("not a astrong number")


num =input()
b = len(num)
sum =0
for i in num:
    sum = sum + int(i) ** b
if sum == num:
    print(" true")
else:
    print("False")



