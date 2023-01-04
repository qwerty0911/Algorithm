n = int(input())
data = list(map(int,input().split()))
data.sort()
m = int(input())
target_list = list(map(int,input().split()))

for i in range(m):
    target = target_list[i]
    midi = m//2
    while True:
        if target>data[-1] or target<data[0]:
            print(0)
            break
        else:
            if data[midi]<target:
                midi+=1
                if data[midi]>target:
                    print(0)
                    break
            elif data[midi]>target:
                midi-=1
                if data[midi]<target:
                    print(0)
                    break
            else:
                print(1)
                break



''' test case
5
4 1 5 2 3
5
1 3 7 9 5
,

6
1 2 3 4 5 6
5
1 9 0 3 10
'''