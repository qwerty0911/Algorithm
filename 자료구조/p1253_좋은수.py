import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
#print(arr)
cnt=0

for find in arr:
    i = 0
    j = N - 1
    while i < j:
        sum = arr[i]+arr[j]
        if sum == find:
            cnt+=1
            # i+=1
            # j-=1
            break
        elif sum>find:
            j-=1
        else:
            i+=1


print(cnt)