import sys

N,M=map(int,input().split())

#print(N,M)
arr=[[0]*(N+1)]

for _ in range(N):
    arr.append([0]+list(map(int,sys.stdin.readline().split())))


#print(arr)

D=[[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    D[1][i+1] = D[1][i]+arr[1][i+1]
    D[i+1][1] = D[i][1]+arr[i+1][1]

#print(D)


for i in range(2,N+1):
    for j in range(2,N+1):
        D[i][j]=D[i][j-1]+D[i-1][j]-D[i-1][j-1]+arr[i][j]

for _ in range(M):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    result = D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1]
    print(result)
