import sys

N=int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
v=int(sys.stdin.readline())

cnt=0
for item in array:
    if item == v:
        cnt+=1

print(cnt)
'''
11
1 4 1 2 4 2 4 2 3 4 4
2
'''