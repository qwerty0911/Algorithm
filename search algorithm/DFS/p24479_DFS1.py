import sys
sys.setrecursionlimit(10 ** 6)

N,M,R =  map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt=0

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()


def DFS(v):
    global cnt
    cnt+=1
    visited[v]=cnt

    for direction in graph[v]:
        if visited[direction] == 0:
            DFS(direction)

DFS(R)
for i in visited[1:]:
    print(i)

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