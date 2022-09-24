import sys
input = sys.stdin.readline
import math


'''
지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결
케빈 베이컨 게임은 임의의 두 사람이 최소 몇단 계 만에 이어질 수 있는지 계산하는 게임.

케빈 베이컨 게임

최단경로들의 합이 최소인애를 내보내면 될 것같다.
'''
n, m = map(int, input().split()) # 유저수, 친구관계의 수
distance = [[math.inf]*(n) for _ in range(n)]

for i in range(n):
    distance[i][i]=0

for _ in range(m):
    a, b = map(int, input().split())
    distance[a-1][b-1]=1
    distance[b-1][a-1]=1


for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i-1][j-1] = min(distance[i-1][k-1] + distance[k-1][j-1], distance[i-1][j-1])

tmp = []
max_sum =math.inf
for index,a in enumerate(distance):
    tmp.append(sum(a))

min_sum = min(tmp)

index_list = []
index_list.append(tmp.index(min_sum)+1)

print(min(index_list))
# print(tmp)
# print(min(tmp))













