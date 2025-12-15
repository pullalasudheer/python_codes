'''def checkhcf(x,y):
    smallest =0
    if x<y:
        smallest =x
    else:
        smallest =y

    hcf =0
    for i in range(1, smallest+1):
        if (x % i ==0) and (y % i ==0):
            hcf=i
    return hcf
x = 12
y= 14
print("The HCF of  numbers is {} and {} is {}".format(x,y,checkhcf(x,y)))
'''

'''def checkhcf(x,y):
    while(y>0):
        x,y = y,(x%y)
    return x
x=12
y=14
print("The HCF i 2 numbers {} and {} is {}".format(x,y,checkhcf(x,y)))
'''

#reverse a string or number

str = "sudheer"
str1 =" "


