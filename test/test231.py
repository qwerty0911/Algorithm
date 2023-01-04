import random


def addNum(times):
    result=[]
    for _ in range(times):
        result.append(random.randint(1,10000))

    return result

n=int(input("응모자수 :"))
sortedArr = sorted(addNum(n))

n=[1]*10000
for i in range(1,10000):
    n[i]=i

for i in sortedArr:
    if i in n:
        n.remove(i)

print(min(n))






#558, 791, 3491, 984