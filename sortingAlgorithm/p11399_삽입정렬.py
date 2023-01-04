import sys
n = int(input())
inputArr = list(map(int, sys.stdin.readline().split()))

for i in range(1,n):
    insert_point = i
    insert_value = inputArr[i]
    # for j in range(i-1,-1,-1):
    #     if inputArr[j] < insert_value:
    #         insert_point=j+1
    #         break
    #     if j==0:
    #         insert_point=0
    for j in range(i):                      #정렬된 영역
        if inputArr[j] > insert_value:
            insert_point=j
            break
    for j in range(i,insert_point, -1):
        inputArr[j] = inputArr[j-1]
    inputArr[insert_point] = insert_value

print(inputArr)

s=[0]*n
s[0]=inputArr[0]
for i in range(1,n):
    s[i]=s[i-1]+inputArr[i]

print(sum(s))