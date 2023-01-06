import sys
input = sys.stdin.readline

test_case = 1
while True:
    tmp = list(input().rstrip())
    if '-' in tmp:
        break

    left_cnt = 0
    right_cnt= 0

    res_cnt = 0 # 결과값
    for i in range(len(tmp)//2): # 절반까지만!!!
        if tmp[i]=='{':
            left_cnt+=1
        else:
            right_cnt+=1

        # 왼쪽 괄호가 일단 무조건 오른쪽 괄호개수보다 많아야한다.
        if left_cnt<right_cnt:
            tmp[i] = '{' # 이걸로 바꿔주고
            res_cnt+=1
            left_cnt+=1 # 값 다시 갱신
            right_cnt-=1 # 값 다시 갱신



    # 그리고 절반으로 나눠서 절반 기준으로 왼쪽과 다른 것만큼 오른쪽을 바꿔준다.
    left_list = tmp[:(len(tmp))//2]
    right_list = tmp[(len(tmp))//2:]

    # print(left_list)
    # print(right_list)

    for k in range(len(left_list)):
        if left_list[k]== right_list[len(right_list)-1-k]: # 같은거면 +1씩 -> 괄호 매칭이 되어야하므로
            res_cnt+=1


    print(f"{test_case}. {res_cnt}")



    test_case+=1




'''정답코드'''

# answer = []
#
# while True:
#     stack = []
#     count = 0
#     s = input()
#     if '-' in s:
#         break
#     for i in range(len(s)):
#         if not stack and s[i] == '}':
#             count += 1
#             stack.append('{')
#         elif stack and s[i] == '}':
#             stack.pop()
#         else:
#             stack.append(s[i])
#     count += len(stack)//2
#     answer.append(count)
#
# for i in range(len(answer)):
#     print(i+1, '. ', answer[i], sep='')