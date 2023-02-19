x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp)
print(max(dp))

rank=1
while rank < max(dp):
    for i in range(len(dp)):
        if dp[i] == rank:
            print(arr[i],end=' ')
            rank+=1
            continue
