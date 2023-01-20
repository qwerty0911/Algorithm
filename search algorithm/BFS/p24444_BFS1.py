import collections
import sys

N,M,R =  map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
result = [0]*(N+1)

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

def BFS(v):
    queue = collections.deque()
    queue.append(v)
    visited[v]=True
    cnt=1
    while queue:
        nowNode = queue.popleft()
        result[nowNode]=cnt
        cnt+=1
        for e in graph[nowNode]:
            if visited[e]==False:
                queue.append(e)
                visited[e]=True

BFS(R)
for _ in result[1:]:
    print(_)

'''
7 8 1
1 2
1 3
1 4
2 4
1 5
5 6
4 6
6 7
'''