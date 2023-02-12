#Longest Common subsequenc
import sys

string1 = "0"+sys.stdin.readline()
string2 = "1"+sys.stdin.readline()
M=len(string1)
N=len(string2)

array = [[0]*(M-1) for _ in range(N-1)]

for i in range(1,N-1):
    for j in range(1,M-1):
        if string1[j] != string2[i]:
            array[i][j] = max(array[i - 1][j], array[i][j - 1])
        else:
            array[i][j] = array[i - 1][j-1]+1

print(array[-1][-1])