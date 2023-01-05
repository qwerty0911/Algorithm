import sys

sentence = sys.stdin.readline().split("-")

print(sentence)
def mySum(array):
    sum=0
    tmp = str(array).split('+')
    for e in tmp:
        sum+=int(e)
    return sum

result=0
for i in range(len(sentence)):
    if i == 0:
        result+=mySum(sentence[i])
    else:
        result-=mySum(sentence[i])


print(result)
'''
100-40+50+74-30+29-45+43+11
'''