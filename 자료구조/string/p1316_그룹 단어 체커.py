import collections
import sys

n = int(input())
cnt=0

for _ in range(n):
    array = sys.stdin.readline().strip()
    visited=[]
    last = 0
    for i in range(len(array)):
        if last != array[i]:
            if array[i] in visited:
                break
            else:
                visited.append(array[i])
                last=array[i]

        if i==len(array)-1:
            cnt+=1
    #print(visited)


print(cnt)
