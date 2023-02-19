import collections
import copy
import sys

N,M = map(int,sys.stdin.readline().split())
moveX = [0,0,1,-1]
moveY = [-1,1,0,0]
minimap=[]

for _ in range(N):
    minimap.append(list(map(str,sys.stdin.readline().rstrip())))

# print(minimap)

def bfs(i,j):
    max_n=0
    queue = collections.deque()
    minimap[i][j]=0
    queue.append([i,j])
    visit[i][j]=True

    while queue:
        nowX, nowY= queue.popleft()
        for i in range(4):
            newX = nowX+moveX[i]
            newY = nowY+moveY[i]
            if 0 <= newX < N and 0 <= newY < M and visit[newX][newY]==False and minimap[newX][newY] != 'W':
                visit[newX][newY]=True
                queue.append([newX,newY])
                minimap[newX][newY] = minimap[nowX][nowY]+1
                max_n = max(max_n, minimap[newX][newY])

    return max_n

result=0
for i in range(N):
    for j in range(M):
        if minimap[i][j]!='W':
            visit = [[False] * M for _ in range(N)]
            result=max(result,bfs(i,j))

print(result)
