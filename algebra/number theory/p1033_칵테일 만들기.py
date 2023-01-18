import sys

N = int(sys.stdin.readline())

array=[[] for _ in range(N)]
visited = [False]*N
D=[1]*N
lcm=1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def DFS(v):
    visited[v]=True

    for i in array[v]:
        next = i[0]
        if visited[next]==False:
            D[next] = D[v] * i[2] // i[1]
            DFS(next)




for _ in range(N-1):
    a,b,p,q = map(int,sys.stdin.readline().split())
    array[a].append((b,p,q))
    array[b].append((a,q,p))
    lcm *= (p*q // gcd(p,q))

D[0] = lcm
#print(array)
DFS(0)
mgcd = D[0]     #D의 최대공약수

for i in range(1,N):
    mgcd = gcd(mgcd,D[i])

for i in range(N):
    print(D[i]//mgcd,end=" ")

'''tc
5
4 0 1 1
4 1 3 1
4 2 5 1
4 3 7 1

5
4 0 1 1
4 1 3 2
4 2 5 1
4 3 7 1
'''