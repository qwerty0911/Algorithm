import collections
import sys

queue=collections.deque()
sequence = []

N,K=map(int,sys.stdin.readline().split())

print("<",end="")
for i in range(N):
    queue.append(i+1)

i=0
while len(queue)>1:
    tmp = queue.popleft()
    if i%K==K-1:
        print(tmp,end=", ")
    else:
        queue.append(tmp)
    i+=1

print("{}>".format(queue.pop()))