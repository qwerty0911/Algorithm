import sys

S,P = map(int, sys.stdin.readline().split())
myString =list(map(str,sys.stdin.readline().rstrip()))
checkList = list(map(int,sys.stdin.readline().split()))
checkSecret=0
myWindow=[]
myList=[0]*4

def add(c):
    global checkList, checkSecret, myList
    if c == 'A':
        myList[0]+=1
    elif c=='C':
        myList[1]+=1
    elif c=='G':
        myList[2]+=1
    else:
        myList[3]+=1

def remove(c):
    pass

for i in myString[:P]:
    add(i)


for i in myString[P:]:
    add(i)
    remove(i)

