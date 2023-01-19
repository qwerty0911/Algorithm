import sys

k = int(sys.stdin.readline())
array=[]
for _ in  range(k):
    a=int(sys.stdin.readline())
    if a==0:
        array.pop()
    else:
        array.append(a)

print(sum(array))