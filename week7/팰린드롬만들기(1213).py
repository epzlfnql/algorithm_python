# 답은 정확히 다 나오는데 어떤 부분이 틀렸는지 모르겠다.
# d <-처럼 한개만 나온경우를 고려안해줘서..?
# 다른 사람 코드 홀수개가 한개만 나온경우를 고려안해준거같은데 확인해보자

import sys
input = sys.stdin.readline

tmp = list(map(str, input().strip()))


tmp.sort() # 알파벳 순서대로 정렬


# 딕셔너리를 선언해 알파벳과 개수 추가
count = {}
for s in tmp:
    if s in count:
        count[s]+=1
    else:
        count[s]=1


# 짝수의 개수, 홀수의 개수가 몇개인지 알아보기 위해
count_list = list(count.values()) # 각 키의 개수들을 반환
count_even =0
count_odd = 0
for i in count_list:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1



result = '' # 반씩 반씩 더해서 출력할 예정
tmp2 = []
if count_odd >1:
    print("I'm Sorry Hansoo")
else:
    if count_odd==1 and count_even==0: # d처럼 한개만 홀수개수 한개만 나온경우
        print(tmp[0]*len(tmp))
    else:
        for s in count:
            if count[s]%2==0:# 짝수개면
                result+=s*(count[s]//2)
            else: # 홀수개면
                result+=s*(count[s]//2)
                tmp2.append(s)
        if len(tmp2)!=0: # tmp2가 비어있지 않은경우, 즉 홀수 개수가 1개 나온 경우
            result = result + tmp2[0]+result[::-1]
            print(result)
        else:
            print(result+result[::-1])



