n,m = map(int,input().split())
lessons = list(map(int,input().split()))

start = lessons[-1]
end = sum(lessons)

while start<=end:
    mid = (start+end)/2
    for _ in n:
        pass