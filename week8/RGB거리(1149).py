# 집이 N개
# 1번부터 N번 집이 순서대로 있고
# 거리는 선분으로 나타내고

# 집은 빨, 초, 파 중 하나의 색으로 칠한다.
# 각각의 집을 빨, 초, 파로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구하기
# 1번집의 색은 2번집의 색과 다르다.
# N번 집의 색은 N-1번 집의 색과 다르다.
# i번 집의 색은 i-1, i+1번 집의 색과 다르다.

import sys
input = sys.stdin.readline

N = int(input())

cost_sum = []

for _ in range(N):
    cost_sum.append(list(map(int, input().split()))) # Red_cost, Green_cst, Blue_cost


for i in range(1, N): # 처음꺼는 건들 필요가 없다.
    cost_sum[i][0] = min(cost_sum[i][0]+cost_sum[i-1][1], cost_sum[i][0]+cost_sum[i-1][2])
    cost_sum[i][1] = min(cost_sum[i][1]+cost_sum[i-1][0], cost_sum[i][1]+cost_sum[i-1][2])
    cost_sum[i][2] = min(cost_sum[i][2]+cost_sum[i-1][1], cost_sum[i][2]+cost_sum[i-1][0])

print(min(cost_sum[N-1][0], cost_sum[N-1][1], cost_sum[N-1][2]))

