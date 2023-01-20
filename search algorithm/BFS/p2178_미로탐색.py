import collections
import sys

N, M = map(int,sys.stdin.readline().split())
miro = []
for _ in range(N):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))

movex=[-1,0,1,0]
movey=[0,1,0,-1]


def BFS(x,y):
    queue=collections.deque()
    queue.append([x,y])

    while queue:
        now=queue.popleft()
        for i in range(4):
            nx = now[0]+movex[i]
            ny = now[1]+movey[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if miro[nx][ny]==1:
                    queue.append((nx,ny))
                    miro[nx][ny]=miro[now[0]][now[1]]+1

BFS(0,0)
# print(miro)
print(miro[N-1][M-1])

'''
4 6
101111
101010
101011
111011
'''