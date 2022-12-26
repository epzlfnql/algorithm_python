'''
어떤 나라에 N개의 도시
일직선 도로 위에
원 안에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격
도로 위에 있는 숫자는 도로의 길이 표시

'''

import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
length = list(map(int, input().split())) # 도로의 길이
cost = list(map(int, input().split())) # 도시의 리터당 가격

# 기름값이 최소인 도시 찾아서 인덱스 구하기
# 그 이후부터 쭉 곱하면 도니ㅣ깐

real_cost = cost[:-1] # 맨마지막 도시의 비용은 고려할 필요 없음


result = real_cost[0] * length[0] # 맨처음꺼는 계산해주기
min_cost =real_cost[0] # 고정할거, 이것보다 더 작은게 나오면 갱신해줄 것이다.

for i in range(1, len(real_cost)):
    if real_cost[i]<=min_cost:
        min_cost = real_cost[i]

    result+=length[i] * min_cost


print(result)

# min_index = real_cost.index(min(real_cost))
#
#
# result =0
# for i in range(len(real_cost)):
#     if i>=min_index:
#         result+= real_cost[min_index] * length[i]
#     else:
#         result+= real_cost[i] * length[i]




