import sys

num1, num2 = map(int,sys.stdin.readline().split())

def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)

# print(gcd(num1,num2))

for _ in range(gcd(num1,num2)):
    print('1',end="")