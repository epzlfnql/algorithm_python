'''
방향 없는 그래프
연결 요소의 개수가 구하는 프로그램
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수

visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(v):
    que = deque([v])
    visited[v] = 1 # 방문 표시하고

    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i]==0: # 아직 방문안했으면
                visited[i]=1 # 방문 표시해주고
                que.append(i)




res = 0
for i in range(1, n+1):
    if visited[i] ==0: # 아직 방문안했으면
        bfs(i)
        res+=1 # 하나도 포함안되어 있으면 연결된게 없는 하나의 개체
print(res)


