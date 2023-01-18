import collections
import sys

N,M,K,X = map(int,sys.stdin.readline().split())
#도시수, 도로수, 거리정보, 출발도시 번호

visited  = [0]* (N+1)
graph  = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)

#print(graph)

def BFS(v):
    queue = collections.deque()
    queue.append(v)

    while queue:
        nowNode = queue.popleft()
        for i in graph[nowNode]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[nowNode]+1

BFS(X)
#print(visited)
isExist = False

for i in range(len(visited)):
    if visited[i] == K:
        print[i]
        isExist=True
        break

if isExist == False:
    print(-1)


'''
4 4 2 1
1 2 
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4
'''