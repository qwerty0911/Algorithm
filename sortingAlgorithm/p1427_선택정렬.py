import sys

inputArr = list(map(int,sys.stdin.readline().rstrip()))

print(inputArr)

for i in range(len(inputArr)):
    max = i
    for j in range(i+1,len(inputArr)):  #정렬되지 않은 부분에서 최대값 찾기
        if inputArr[j] > inputArr[max]:
            max = j

    if inputArr[i] < inputArr[max]:     #정렬된 부분의 오른쪽값과 최대값 스왑
        inputArr[i],inputArr[max] = inputArr[max], inputArr[i]
        # tmp = inputArr[i]
        # inputArr[i] = inputArr[max]
        # inputArr[max] = tmp
    print(inputArr)

print(inputArr)
