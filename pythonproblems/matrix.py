'''x=[[2,3],[5,6],[7,9]]
result=[[0,0,0],[0,0,0]]
for i in  range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]
for r in result:
    print(r)
    '''

x=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
y =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] *y[j][k]
for r in result:
    print(r)