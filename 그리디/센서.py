'''
N개의 센서
K개의 집중국
각 집중국의 수신 가능 영역의 길이의 합을 최소화
'''

import sys
import math
input = sys.stdin.readline

n = int(input()) # 센서의 개수
k = int(input()) # 집중국 개수
location = list(map(int, input().split()))


location.sort()

result = math.inf # 가장 큰값으로 일단 초기화

# 이분탐색 문제인가?

# 아니다 일단 차이를 보며주는거에서 sort(reverse=True로 상위 k개만큼 리스트를 나눈다.
diff_list = []
for i in range(1, n):
    diff_list.append(location[i]-location[i-1])
sorted_diff_list = sorted(diff_list, reverse=True)

print(location)
print(diff_list)
print(sorted_diff_list)

tmp_list = [] # 나눠준 리스트를 저장해주는 것.
idx_list = []
for i in range(k-1): # k-1개만큼 차이많은 인덱스 찾기 -> 리스트 나눠줄거임
    idx_list.append(diff_list.index(sorted_diff_list[i]))

start = 0
for i in idx_list:

    tmp_list.append(location[start:i+1])
    start = i
    if i==idx_list[-1]: # 맨마지막 인덱스일 경우
        tmp_list.append(location[start+1:]) #
print(tmp_list)


# 리스트 개수만큼 최소값을 반환하는거 구하기
realreal_result = 0

for lst in tmp_list:
    start = lst[0]
    end = lst[-1]

    min_result = math.inf
    while start <=end:
        mid = (start+end)//2 # 이분탐색 진행
        tmp_result = 0
        for i in lst:
            tmp_result += abs(mid - i)
        if tmp_result <= min_result:
            min_result = tmp_result
            end = end-1 # 이거 기준없음
        else:
            start = start+1 # 이것도 기준이 없음ㅋㅋ
    print(min_result)
    realreal_result+=min_result

print(f'왜 6이 아니라 5가 답이냐고 : {realreal_result}')
# for i in range(len(location) - k+1): # n-k+1 번만큼 반복문
#
    # 맨마지막값과 맨처음값 뺀만큼


# 1, 3, 6, 6, 7, 9
# 간격 : [2, 3, 0, 1, 2]
# 답 : 2, 6


# 3, 6, 7, 8, 10, 12, 14, 15, 18, 20
# 답 :