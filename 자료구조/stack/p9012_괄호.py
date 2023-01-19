import sys

T = int(sys.stdin.readline())
#array = [[] for _ in range(T)]



for i in range(T):
    # print('#',int(i+1))
    array=list(map(str,sys.stdin.readline().rstrip()))
    stack = []
    isVPS = True
    for c in array:
        if c == '(':
            stack.append(1)
        else:
            try:
                stack.pop()
            except:
                print('NO')
                isVPS=False
                break

    if isVPS==True:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')