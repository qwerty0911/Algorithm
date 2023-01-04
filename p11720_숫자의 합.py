import sys

n = sys.stdin.readline()
# numbers = list(map(int,sys.stdin.readline().rstrip()))
numbers = list(input())


sum=0

for i in numbers:
    sum+=int(i)

print(sum)