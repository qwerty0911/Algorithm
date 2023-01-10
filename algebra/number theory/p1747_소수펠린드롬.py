N = int(input())
A = [0]*10_000_000

for i in range(10_000_000):
    A[i] = i

for i in range(2,int(10_000_000**0.5)+1):
    if A[i]==0:
        continue
    for j in range(2*i,10_000_000,i):
        A[j] = 0

def isPelindrome(num):
    tmpArray = list(str(num).rstrip())
    s=0
    e=len(tmpArray)-1
    while e>s:
        if tmpArray[s]!=tmpArray[e]:
            return False
        s+=1
        e-=1
    return True

for i in range(N,10_000_000):
    if A[i] != 0:
        if isPelindrome(i):
            print(i)
            break
