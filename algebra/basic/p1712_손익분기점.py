import sys

A,B,C=map(int,sys.stdin.readline().split())

if C==B:
    print(-1)
else:
    result = A//(C-B)
    if result >= 0:
        print(result+1)
    else:
        print(-1)

