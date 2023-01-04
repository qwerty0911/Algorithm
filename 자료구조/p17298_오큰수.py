import sys

N = int(input())
answer = [0]*N
inputArr = list(map(int, sys.stdin.readline().split()))
myStack = []

for i in range(N):
    #
    while myStack and inputArr[myStack[-1]] < inputArr[i]:
        answer[myStack.pop()] = inputArr[i]
    myStack.append(i)

while myStack:
    answer[myStack.pop()] = -1

result = ""

for i in range(N):
        result += str(answer[i])+" "

print(result)