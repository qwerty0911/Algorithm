n,m = map(int,input().split())
A=[0]*(m+1)

for i in range(m+1):
    A[i] = i

i=2
while i<m**0.5+1:
    j=2
    while i**j<m:
        A[i**j]=0
        j+=1
    i+=1

cnt=0
for i in A[n:]:
    if i != 0:
        cnt+=1

print(cnt)