from collections import deque

node,edge,start = map(int, input().split())

print(node,edge,start)
graph=[[] for _ in range(node+1)]
visited = [False]*(node+1)

for _ in range(edge):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(n):
    visited[n]=True
    print(n,end=' ')

    graph[n].sort()
    for e in graph[n]:
        if not visited[e]:
            DFS(e)



def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=" ")
        for e in graph[now_Node]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)
                print(queue)

DFS(start)
print()
visited = [False]*(node+1)
BFS(start)