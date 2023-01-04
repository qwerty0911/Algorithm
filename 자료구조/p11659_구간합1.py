import sys

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

prefix_sum=[0]

for i in range(len(nums)):
    prefix_sum.append(prefix_sum[i]+nums[i])

#print(prefix_sum)

for _ in range(M):
    start,end = map(int,sys.stdin.readline().split())
    print(prefix_sum[end]-prefix_sum[start-1])