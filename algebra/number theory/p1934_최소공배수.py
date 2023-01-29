import sys

T = int(input())

for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    tmp = a*b
    while a%b!=0:
        remain = a%b
        a=b
        b=remain

    print(tmp//b)