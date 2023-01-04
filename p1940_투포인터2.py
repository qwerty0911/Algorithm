import sys

N = int(input())
M = int(input())
arr = list(map(int, sys.stdin.readline().split()))
first = 0
second = N-1
cnt=0

arr.sort()
print(arr)

while first<second:
    # print(arr[first], arr[second])
    if arr[first]+arr[second]==M:
        cnt+=1
        first+=1
        second-=1
        # print("right!!")
    elif arr[first]+arr[second]<M:
        first+=1
    else:
        second-=1

print(cnt)