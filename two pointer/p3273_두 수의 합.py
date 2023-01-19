import sys

n = int(input())
array = list(map(int,sys.stdin.readline().split()))
x = int(input())

array.sort()
#print(array)

i=0
j=len(array)-1
cnt=0
while i<j :
    if array[i]+array[j]>x:
        j-=1
    elif array[i]+array[j]<x:
        i+=1
    else:
        cnt+=1
        i+=1
        j-=1

print(cnt)