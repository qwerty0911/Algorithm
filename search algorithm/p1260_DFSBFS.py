import collections
import sys

N,M,V = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N+1):
    graph[i].sort()

def DFS(v):
    visited[v]=True
    print(v,end=' ')
    for e in graph[v]:
        if visited[e] is False:
            DFS(e)

def BFS(v):
    queue = collections.deque()
    queue.append(v)
    visited[v]=True
    print(v,end=' ')

    while queue:
        nowNode = queue.popleft()
        for e in graph[nowNode]:
            if visited[e] is False:
                visited[e] = True
                queue.append(e)
                print(e,end=' ')

visited = [False]*(N+1)
DFS(V)
print()
visited = [False]*(N+1)
BFS(V)