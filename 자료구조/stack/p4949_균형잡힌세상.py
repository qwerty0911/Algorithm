import sys
i=1
while True:
    strings = list(map(str, sys.stdin.readline().rstrip()))
    if strings == ['.']:
        break

    isVPS = True
    stack = []
    for c in strings:

        if c == '(' or c=='[':
            stack.append(c)

        elif c==')':
            if not stack or stack[-1]=='[':
                isVPS = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif c==']':
            if not stack or stack[-1] == '(' :
                isVPS = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if isVPS and not stack:
        print('yes')
    else:
        print('no')

