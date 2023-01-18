import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]
answer = [0]*(N+1)  #신뢰도 리스트

for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        nowNode = queue.popleft()
        for i in graph[nowNode]:
            if visited[i] == False:
                queue.append(i)
                answer[i]+=1

for i in range(N+1):
    visited = [False] * (N + 1)
    BFS(i)

# print(answer)
max = 0
for i in answer:
    if i > max:
        max = i

for i in range(len(answer)):
    if answer[i] == max:
        print(i, end=' ')

'''
5 4
3 1
3 2
4 3
5 3
'''