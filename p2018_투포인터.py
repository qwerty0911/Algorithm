N = int(input())

cnt =1
start_index=1
end_index=1
sum=1

while end_index != N:
    if sum == N:
        cnt+=1
        end_index+=1
        sum+=end_index

    elif sum > N:
        sum-=start_index
        start_index+=1

    else:
        end_index+=1
        sum+=end_index

print(cnt)

