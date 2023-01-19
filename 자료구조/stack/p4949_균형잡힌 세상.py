import sys
i=1
while True:
    strings = list(map(str, sys.stdin.readline().rstrip()))
    stack=[]
    isVPS = True
    if strings == ['.']:
        break
    else:
        for c in strings:
            if c == '(':
                stack.append('(')
            elif c=='[':
                stack.append('[')
            elif c==')':
                try:
                    tmp = stack.pop()
                    if tmp == '[':
                        print('NO')
                        isVPS = False
                        break
                except:
                    print('NO')
                    isVPS = False
                    break
            elif c==']':
                try:
                    tmp = stack.pop()
                    if tmp == '(':
                        print('NO')
                        isVPS = False
                        break
                except:
                    print('NO')
                    isVPS = False
                    break

    if isVPS:
        if len(stack)==0:
            print('YES')

