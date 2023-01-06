numOfCity = int(input())
numOfNosun = int(input())
distance = [[10000*numOfNosun+1]*(numOfCity+1) for _ in range(numOfCity+1)]

# graph = [[] for _ in range(numOfCity+1)]

# for _ in range(numOfNosun):
#     start,end,weight = map(int,input().split())
#     graph[start].append([end,weight])

# print(graph)

for i in range(0,numOfCity+1):
    distance[i][0] = 0
    distance[0][i] = 0
    distance[i][i] = 0


for _ in range(numOfNosun):     #인접 도시를 잇는 노선정보 저장
    start, end, weight = map(int, input().split())
    if distance[start][end] > weight:
        distance[start][end] = weight

for k in range(1,numOfCity+1):
    for i in range(1,numOfCity+1):
        for j in range(1,numOfCity+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1,numOfCity+1):
    for j in range(1,numOfCity+1):
        if distance[i][j] == 10000*numOfNosun+1:
            print(0,end=" ")
        else:
            print(distance[i][j], end=" ")
    print()


'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''