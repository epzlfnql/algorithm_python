'''
1부터 N까지의 수로 이루어진 순열

'''
import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int, input().split(' ')))

# 오르차순 정렬된 인풋 == 사전순으로 가장 처음에 오는 순열
sort_input = sorted(input_list)

if sort_input == input_list:
    print(-1)

for i in range(len(input_list)-2, -1, -1): # 거꾸로서부터
    if input_list[i+1] < input_list[i]:

        right_tmp = input_list[i+1:] # 오른쪽 모두를 일단 임시저장

        # print(right_tmp)
        # print(input_list[:i])

        tmptmp = sorted(right_tmp, reverse = True)

        for j in tmptmp:
            if j < input_list[i]:
                idx = input_list.index(j) # 기준점에서 오른쪽 배열에서 기준보다 작으면서 가장 큰값 인덱스
                input_list[idx] = input_list[i] # 값 switch
                input_list[i] = j

                # print(input_list)

                # 오른쪽 내림차순 정렬
                result = input_list[:i+1] + sorted(input_list[i+1:], reverse=True)
                for t in result:
                    print(t, end = ' ')
                break



        break






