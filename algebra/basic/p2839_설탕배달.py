N = int(input())

if N==1 or N==2 or N==4 or N==7:
    quot=-1
    remain=-1
else:
    quot = N//5
    remain = N%5

if remain==1 or remain==3:
    quot+=1
elif remain==2 or remain==4:
    quot+=2

print(quot)

