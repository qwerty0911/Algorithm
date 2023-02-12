import collections
import sys

N = int(sys.stdin.readline())

RGBArray=[]
RBArray=[[0]*N for _ in range(N)]

movex=[1,-1,0,0]
movey=[0,0,1,-1]

for i in range(N):
    inputList = list(map(str,sys.stdin.readline().strip()))
    RGBArray.append(inputList)

for i in range(N):
    for j in range(N):
        if RGBArray[i][j]=='B':
            RBArray[i][j] ='B'
        else:
            RBArray[i][j] = 'R'


def BFS(array, x, y, color):
    queue= collections.deque()
    queue.append((x,y))

    while queue:
        now = queue.popleft()
        x=now[0]
        y=now[1]
        for i in range(4):
            nx = x+movex[i]
            ny = y+movey[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if array[nx][ny]==color:
                    queue.append((nx,ny))
                    array[nx][ny]=0

#노색맹
cnt = 0
for i in range(N):
    for j in range(N):
        if RGBArray[i][j] != 0:
            BFS(RGBArray,i, j, RGBArray[i][j])
            cnt += 1

print(cnt,end=' ')

#색맹
cnt = 0
for i in range(N):
    for j in range(N):
        if RBArray[i][j] != 0:
            BFS(RBArray, i, j, RBArray[i][j])
            cnt += 1

print(cnt)

'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''