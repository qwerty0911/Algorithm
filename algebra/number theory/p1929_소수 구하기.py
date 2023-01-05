m,n = map(int,input().split())
A=[0]*(n+1)

for i in range(m,n+1):
    A[i]=i

for i in range(2,int((n+1)**0.5+1)):
    for j in range(i*2,n+1,i):
        A[j] = 0

for item in A:
    if item:
        print(item)


