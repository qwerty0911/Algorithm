import sys

node,edge=map(int,input().split())

A=[[] for _ in range(node+1)]
visited = [False]*(node+1)

for _ in range(edge):
    s,e = map(int,input().split())
    A[s].append(e)      #양반향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)

print(A)

def DFS(v):
    visited[v]=True
    print(v)
    for e in A[v]:
        if not visited[e]:
            DFS(e)

count = 0

for i in range(1,node+1):
    if visited[i] == False:
        DFS(i)
        count+=1

print("연결요소의 수 : ",count)