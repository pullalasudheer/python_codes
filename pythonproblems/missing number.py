'''num =[1,3,4]
b = len(num)
total = b*(b+1)//2
res=sum(num)-total
print("missing number:",res)
'''
def find_the_missing (arr,n):
    total_sum = n * (n+1)//2
    total_arr= sum(arr)
    return total_sum - total_arr
arr =[1,2,4,5,6]
n =6
print("missing value:",find_the_missing(arr,n))