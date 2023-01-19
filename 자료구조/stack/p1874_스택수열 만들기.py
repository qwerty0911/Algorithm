import sys

N = int(input())
inputArr = list(map(int, sys.stdin.readline().split()))

stack = []
num = 1
result = True
answer = ''

for i in range(N):
    su = inputArr[i]
    if su >= num: #현재 수열값 >= 오름차순 자연수 : 값이 같아질때까지 append()
        while su >= num:
            stack.append(num)
            num +=1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else: #현재 수열값 < 오름차순 자연수: pop()을 수행해 수열 원소 꺼냄
        n = stack.pop()
        if su<n:
            print('NO')
            result = False
            break
        else:
            answer += '-\n'

if result:
    print(answer)
