'''str1="heart"
str2="earth"
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("It is a anagram")
    else:
        print("it is not a amagram")
else:
    print("it is not a anagram")
    '''
num = int(input("Enter the number:"))
temp =  num
b = len(str(num))
sum =0
while temp > 0:
    digit = temp %10
    sum = sum + digit ** b
    temp = temp // 10
if sum == temp:
    print("it is amstrong number")
else:
    print("it is not a amstrong number")
