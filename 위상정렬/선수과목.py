'''
선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수
선수과목 조건을 지킬경우 각각의 전공과목을 언제 이수할 수 있는지 궁금해졌다.
1. 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
2. 모든 과목은 매 학기 항상 개설된다.

모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는지 계싼하는 프로그램을 작성해라
'''
import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split()) # n은 과목의 수, m은 선수 조건의 수

graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
result = [1]*(n+1)
dQ = deque()


for _ in range(m):
    a, b = map(int, input().split())

    graph[a][b]=1
    degree[b]+=1


# print(degree)

for i in range(1, n+1):
    if degree[i]==0: # 차수가 0이면, 선행해야할 작업이 없으니까 큐에 넣는다.
        dQ.append(i)

while dQ: # 큐가 빌때까지
    x = dQ.popleft()
    # print(x, end=' ')

    for i in range(1, n+1):
        if graph[x][i]==1: # x로 시작해서 i도착하는 경로가 있으면
            degree[i]-=1
            result[i] = result[x]+1

            if degree[i]==0:
                dQ.append(i)

for i in range(1, len(result)):
    print(result[i], end= ' ')