
n = int(input())
A = [[] for _ in range(n)]

for i in range(n):
    A[i]=list(map(int,input().split()))

sorted(A,key = lambda x:(x[1],x[0]))

tmp = 0
cnt=0
print(A)

for (start,end) in A:
    if start >= tmp:
        tmp = end
        cnt+=1

print(cnt)

''' test case
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8  12
2 13
12 14
'''