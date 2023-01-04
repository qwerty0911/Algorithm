import sys

n = int(input())
inputArr=[]

for _ in range(n):
    inputArr.append(int(sys.stdin.readline()))

# print(inputArr)

for i in range(n)[::-1]:
    for j in range(i):
        if inputArr[j] > inputArr[j+1]:
            inputArr[j],inputArr[j+1] = inputArr[j+1],inputArr[j]

print(inputArr)