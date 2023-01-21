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




def bfs(v, cnt):

    que = deque()
    que.append([v])
    visited[v]=1

    while que:
        v = que.popleft()
        cnt += 1

        for k in graph[v]:
            print(k)
            if visited[k] == 0:  # 아직 방문안했으면
                visited[k] = 1  # 방문 표시해주고
                que.append(k)
    return cnt


cnt = 0


cnt = bfs(1, cnt)
print(cnt)


