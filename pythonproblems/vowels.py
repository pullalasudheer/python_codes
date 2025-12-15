def countvowels(text):
    vowels = "aeiouAEIOU"
    count =0
    for c in text:
        if c in vowels:
            count +=1
        return count
text = input("Enter the numbers:")
print("Number of vowels",countvowels(text))


'''num = str(123)
b = len(str(num))
temp = num
sum =0
for i in num:
    sum = sum + int(i) ** b
if sum == temp:
    print(" it is a amstrong number")
else:
    print(" it is not a amstrong number")
    '''