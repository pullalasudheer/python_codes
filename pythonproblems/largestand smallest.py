'''n=[1,2,3,4,5,6,7]
n.sort()

smallest = n[0]
largest = n[6]
print("the largest num is {}".format(largest))
print("the smallest num is {}".format(smallest))
'''
n =[1,2,3,4,5]
large = 0
small=n[0]
for i in n:
    if i >large:
        large =i
    elif i < small:
        small= i
print("Large",large )
print("small",small)