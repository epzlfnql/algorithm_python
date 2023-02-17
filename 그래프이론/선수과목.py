'''어떤 과목들은 선수과목이 있다.
선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수할 수 있는지
'''

import sys
from collections import deque

n, m = map(int, input().split()) # 과목 개수, 선수 조건의수(간선의 수)

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)

outdegree = [1] * (n+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split()) # a번 과목이 b번 과목의 선수과목
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b]+=1


# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -=1
            outdegree[i] = outdegree[now]+1 # 그 전에꺼에서 +1만 해주면 된다. 약간 dp 느낌?
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    # for i in result:
    #     print(i, end=' ')

topology_sort()

for i in range(1, n+1):
    print(outdegree[i], end= ' ')