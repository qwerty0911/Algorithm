import sys

N = int(sys.stdin.readline())
paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j]+=1

cnt=0

for i in range(100):
    for j in range(100):
        if paper[i][j] >0:
            cnt+=1

print(cnt)

