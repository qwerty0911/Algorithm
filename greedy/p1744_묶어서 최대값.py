from queue import PriorityQueue
N=int(input())
positivePq = PriorityQueue()
negativePq = PriorityQueue()
zeroCnt=0
oneCnt=0


for _ in range(N):
    data = int(input())
    if data == 0:
        zeroCnt+=1
    elif data ==1:
        oneCnt +=1
    elif data>0:
        positivePq.put(data*-1)
    else:
        negativePq.put(data)

sum=0

while positivePq.qsize() > 1:
    data1 = positivePq.get()
    data2 = positivePq.get()
    sum+=data1*data2

if positivePq.qsize()==1:
    sum+=positivePq.get()*-1

while negativePq.qsize()>1:
    data1 = negativePq.get()
    data2 = negativePq.get()
    sum+=data1*data2

if negativePq.qsize()==1:
    if zeroCnt==0:
        sum+=negativePq.get()

print(sum+oneCnt)


'''
9
-1
-8
1
2
3
6
-5
0
1
'''