n,total = map(int,input().split())
coins = []
cnt=0

for _ in range(n):
    coins.append(int(input()))

for i in coins[::-1]:
    cnt+=total//i
    total%=i

print(cnt)

''' test case
10 4200
1
5
10
50
100
500
1000 
5000
10000
50000
,

10 4270
1
5
10
50
100
500
1000 
5000
10000
50000
'''