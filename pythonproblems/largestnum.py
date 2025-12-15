"find the largest  number amoung these three input numbers"

'''
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
num3=int(input("Enter the number:"))

if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
    print("largest number is:",largest)
'''



num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))
num3 = int(input("Enter the number3:"))

if (num1 >= num2) and (num1>= num3):
    largest = num1
elif(num2>=num1) and (num2>=num3):
    largest = num2
elif(num3>=num1) and (num3>=num2):
    largest = num3
    print("largest number is:",largest)