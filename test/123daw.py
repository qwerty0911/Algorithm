def solution(string):
    answer = [[] for _ in range(len(string))]

    for i in range(len(string)):
        print("i:",i)
        while True:
            for j in range(len(string[i][:-2])):
                print("j:",j)
                if string[i][j:j + 3] == '111':
                    for k in range(j + 2, len(string[i][:-2])):
                        print("k:",k)
                        if string[i][k:k + 3] == '110':
                            tmp = string[i][:j] + "110" + string[i][j:]
                            print(tmp," and ")
                            string[i] = tmp
                        else:
                            if k == len(string[i][-3]):
                                break

                if j == len(string[i][-3]):
                        break
    answer = string
    return answer

print(solution(	["1110", "100111100", "0111111010"]))