import sys

n=int(input())
A=list(map(int, sys.stdin.readline().split()))

def quicsort(s,e,array):
    pivot = array[e-1]
    start=s
    end=e-2
    while(start>end):
        if array[start]<pivot:
            start+=1
        elif array[end]>pivot:
            end-=1
        elif array[start]>pivot and array[end]<pivot:
            array[start],array[end]=array[end],array[start]
            start+=1
            end-=1
    for i in range(len(array)-1,start,-1):
        array[i], array[i-1] = array[i-1], array[i]

    return array

print(quicsort(0,8,[42,32,24,60,15,5,90,45]))



    

