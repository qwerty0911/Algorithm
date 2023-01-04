import sys
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    i=tmp[0]
    j=1
    while True:
        if tmp[j]==-1:
            break
        graph[i].append((tmp[j],tmp[j+1]))
        j+=2

distance=[0 for _ in range(n+1)]
visited = [False]*(n+1)
# print(graph)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    s=0
    while queue:
        now_Node = queue.popleft()
        for connect,weight in graph[now_Node]: #연결노드,가중치
            if not visited[connect]:
                visited[connect] = True
                queue.append(connect)
                distance[connect]=distance[now_Node]+weight

BFS(1)

maxdis = max(distance)
for i in range(1,n+1):
    if distance[i] == maxdis:
        result = i
        break

distance=[0 for _ in range(n+1)]
visited = [False]*(n+1)
BFS(result)

print("결과 : ",max(distance))

'''
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
'''
