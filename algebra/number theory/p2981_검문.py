import sys

N = int(sys.stdin.readline())

def gcm(a,b):
    if a%b==0:
        return b
    else:
        return gcm(b,a%b)

tmp=int(sys.stdin.readline())
tmp2=int(sys.stdin.readline())
sub = abs(tmp2-tmp)
lgcm = sub

for _ in range(N-2):
    tmp3=int(sys.stdin.readline())
    sub = abs(tmp3-tmp2)
    lgcm = gcm(lgcm,sub)
    tmp2=tmp3

# if lgcm%2==0:
#     for i in range(2,lgcm//2 + 1):
#         if lgcm % i == 0:
#             print(i,end=' ')
# else:
#     for i in range(3, int(lgcm ** 0.5) + 1,2):
#         if lgcm % i == 0:
#             print(i,end=' ')
#
# print(lgcm)
val = []

for i in range(2,int(lgcm**0.5)+1):
    if (lgcm%i)==0:
        val.append(i)
        val.append(lgcm//i)

val.append(lgcm)
val = list(set(val))
val.sort()


for i in val:
    print(i,end=' ')
