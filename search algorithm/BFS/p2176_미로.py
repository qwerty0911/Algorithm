import sys
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m = map(int,input().split())

visited = [[False]*m for _ in range(n)]
miro = []

for _ in range(n):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))

print(miro)
def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j]=True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0]+dx[k]
            y = now[1]+dy[k]
            if x >=0 and y>=0 and x<n and y<m:
                if miro[x][y] !=0 and not visited[x][y]:
                    visited[x][y] = True
                    miro[x][y] = miro[now[0]][now[1]] + 1
                    queue.append((x,y))

BFS(0,0)
print(miro[n-1][m-1])
