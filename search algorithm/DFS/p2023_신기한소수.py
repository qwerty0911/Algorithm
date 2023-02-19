N = int(input())

primeNum=(2,3,5,7)

def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False

    return True


def dfs(n):
    if len(str(n))==N:
        print(n)

    for i in range(10):
        if isPrime(n*10+i):
            dfs(n*10+i)

for i in primeNum:
    dfs(i)