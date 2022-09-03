# 소개팅 회사 들렸다가 x번 회사에 가서 물건 판매
# 1번 회사에 출발하여 K번 회사를 방문한 뒤에 x번 회사로 가는 것이 목표
# 가능한 한 빠르게 이동
# 플로이드 워셜 문제 (n, m의 범위가 100이하이다.)

import sys
input = sys.stdin.readline
INF = int(1e9)


N, M = map(int, input().split()) # 회사의 개수, 경로의 개수
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N+1):
    for b in range(1, N+1):
        if a==b:
            graph[a][b] =0



for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] =1
    graph[b][a] =1

# 거쳐갈 노드 X와 목적지 노드 K를 입력받기
X, K = map(int, input().split())

for a in range(1, N+1):
    for b in range(1,N+1):
        for k in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 1에서 출발해서 k를 지나 X에 도착
result = graph[1][K] + graph[K][X]

# 도달할 수 없는 경우, -1을 출력
if result>=INF:
    print(-1)
else:
    print(result)