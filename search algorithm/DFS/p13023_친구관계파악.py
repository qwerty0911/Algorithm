node,edge=map(int,input().split())
arrive = False
A=[[] for _ in range(node+1)]
visited = [False]*(node+1)

for _ in range(edge):
    f,s = map(int,input().split())
    A[f].append(s)
    A[s].append(f)

print(A)

def DFS(n,depth):
    global arrive
    visited[n] = True
    if depth == 5:
        arrive = True
        return

    else:
        for i in A[n]:
            if not visited[i]:
                DFS(i,depth+1)

for i in range(node):
    DFS(i,1)
    if arrive:
        break


if arrive:
    print(1)
    print(visited)
else:
    print(0)

