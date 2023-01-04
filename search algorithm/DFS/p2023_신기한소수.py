N = int(input())

def isPrime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False

    return True


def DFS(num):
    if len(str(num))==N:
        print(num)

    else:
        for i in range(1,10,2):
            if isPrime(num*10+i):
                DFS(num*10+i)

primeNum=[2,3,5,7]
for i in primeNum:
    DFS(i)
