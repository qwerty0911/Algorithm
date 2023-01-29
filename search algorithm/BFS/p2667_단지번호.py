import collections
import sys

N = int(input())
array=[]
dangi=[0]*(N*N)

mx=[1,-1,0,0]
my=[0,0,1,-1]

for _ in range(N):
    array.append(list(sys.stdin.readline().rstrip()))

def BFS(x,y,cnt=1):
    queue = collections.deque()
    queue.append([x,y])
    array[x][y]=1
    dangi[dangiNum] = cnt

    while queue:
        now = queue.popleft()
        for i in range(4):
            newx = now[0]+mx[i]
            newy = now[1]+my[i]
            if newx>=0 and newx < N and newy >=0 and newy<N:
                if array[newx][newy]=='1':
                    cnt += 1
                    queue.append([newx,newy])
                    array[newx][newy]=cnt
                    dangi[dangiNum]=cnt

dangiNum=0
for i in range(N):
    for j in range(N):
        if array[i][j]=='1':
            BFS(i,j)
            dangiNum += 1

for i in range(N*N):
    if dangi[i]==0:
        print(i)
        index = i
        break

answer = dangi[:i]
answer.sort()
for i in answer:
    print(i)