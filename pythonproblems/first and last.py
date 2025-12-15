list=[1,2,3,4,5,6,1]
def firstandlast(list):
    first = list[0]
    last = list[-1]
    if first == last:
        print("it is same ")
    else:
        print(" it is not same")
print(firstandlast(list))//