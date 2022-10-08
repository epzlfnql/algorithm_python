# 일의 선후관계 유지
# 전체 일의 순서를 짜는 알고리즘
# 진입 차수 : 들어오는거 선의 개수
# 진입 차수가 0인 경우 먼저 시작할 수 있다.
# 진입차수가 1이상이면 먼저 해야할 작업이 있는것.


import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
degree = [0]*(n+1)
dQ = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    degree[b]+=1

for i in range(1, n+1):
    if degree[i]==0: # 차수가 0이면, 선행해야할 작업이 없으니까 큐에 넣는다.
        dQ.append(i)

while dQ: # 큐가 빌때까지
    x = dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)