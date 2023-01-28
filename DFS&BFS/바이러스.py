import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 컴퓨터 수
m = int(input()) # 연결 개수

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a , b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)




def bfs(v):

    que = deque()
    que.append(v)
    visited[v]=1

    while que:
        t = que.popleft()

        for k in graph[t]:
            if visited[k] == 0:  # 아직 방문안했으면
                visited[k] = 1  # 방문 표시해주고
                que.append(k)






bfs(1)
# 방문 안한것만 빼주면 된다 -> 근데 1은 자기자신이므로 1도 빼고
print(sum(visited)-1)


