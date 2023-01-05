#어떤 수가 소수의 n(n>=2)제곱일 때 이 수를 거의소수라고 한다.

m,n = map(int,input().split())
A=[0]*(n+1)

for i in range(m,n+1):
    if i>1:
        A[i]=i

for i in range(2,int((n+1)**0.5+1)):
    for j in range(i*2,n+1,i):
        A[j] = 0

cnt=0
for item in A:
    if item:
        tmp=item
        item*=item
        while item<=n:
            if item < n:
                print(item)
                cnt+=1
            item*=tmp

print(cnt)


