import sys
input = sys.stdin.readline

s = input().strip()


result = ''
if '<' in s:

    index_s = -1
    index_e = -1
    start_index = []
    end_index = []

    cnt = s.count('<')

    while True:
        index_s = s.find('<', index_s+1)
        index_e = s.find('>', index_e+1)

        start_index.append(index_s)
        end_index.append(index_e)

        # 모두 다 돌면 break
        if len(start_index) == cnt :
            break

    # print(start_index)
    # print(end_index)

    for i in range(cnt):
        if i!=cnt-1:
            reverse_str = s[end_index[i]+1:start_index[i+1]]
            tmp = list(map(str, reverse_str.split(' ')))
            reverse_str_final = ''
            for j in range(len(tmp)):
                if j==len(tmp)-1:
                    reverse_str_final+=tmp[j][::-1]
                else:
                    reverse_str_final+=tmp[j][::-1]+' '


            result+=s[start_index[i]:end_index[i]+1]+ reverse_str_final
        else: # 맨마지막 이후
            if len(s)>end_index[-1]+1 :
                result +=  s[start_index[i]:end_index[i] + 1] +s[end_index[i]+1:][::-1]
            else:
                result += s[start_index[i]:end_index[i] + 1]


else: # 있는 그대로 출력
    tmp = list(map(str, s.split(' ')))
    for i in range(len(tmp)):
        if i == len(tmp)-1:
            result+= tmp[i][::-1]
        else:
            result+= tmp[i][::-1]+' '

result = result.strip()
print(result)
