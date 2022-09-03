# N개의 도시
# 단방향
# C라는 도시에서 위급상황 발생 -> 최대한 많은 도시로 메시지를 보내고자 함.
# 메시지를 받게 되는 도시의 개수는 총 몇개이며 도시들이 모두 메시지를 받는데까지 시간은 얼마나 걸리는지
# n, m의 범위가 충분히 크기 때문에, 우선순위 큐를 이용하여 다익스트라 알고리즘을 작성해야 한다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


n, m, c = map(int, input().split()) # 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시 c

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split()) # 도시 x에서 다른도시 y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 z
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))



def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start)) # q에 거리 0, 시작노드 push
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, node = heapq.heappop(q) # 거리와 노드정보 pop
        if distance[node] < dist: #이미 방문한 곳이면
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[node]:
            cost = dist + i[1] # i[1]은 인접 노드까지의 거리
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]: # i[0]은 노드 번호를 나타낸다.
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)

# 도달할 수 있는 노드의 개수
cnt = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance= 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d!= INF:
        cnt+=1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count -1을 출력
print(cnt-1, max_distance)