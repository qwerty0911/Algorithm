import sys

N,M = map(int,sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))

prefix_sum = [nums[0]]*N

for i in range(1,N):
    prefix_sum[i]=prefix_sum[i-1]+nums[i]

cnt=0
prefix_mod=[]
C = [0]*M

for e in prefix_sum:
    prefix_mod.append(e%M)

for i in prefix_mod:
    if i==0:
        cnt+=1
    C[i]+=1

#print(C)

for c in C:
    if c>1:
        cnt+= c*(c-1)//2

print(cnt)