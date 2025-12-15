'''def fact(x):
    f=1
    for i in range(1, x+1):
        f=f *i
    return f
result =fact(6)
print(result)
'''

def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)

result=fact(5)
print(result)