import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]


graph = []
n = int(input())

for _ in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[-1] * n for _ in range(n)] # 일단 -1로 초기화
visited[0][0] = 0
# 최소로 줄이는 거니깐

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1: # 끝까지 도착했을 경우
            return visited[x][y]

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            # 범위내에 있고 아직 방문하지 않은 경우 -> 방문표시
            if 0<= nx < n and 0<= ny<n and visited[nx][ny]==-1:
                if graph[nx][ny]==1: # 흰방일때
                    q.appendleft((nx, ny)) # 값을 왼쪽에입력
                    visited[nx][ny] = visited[x][y]# 흰방일때는 방을 바꿀이유가 없으니깐

                else: # 검은방일때
                    q.append((nx, ny))
                    visited[nx][ny]=visited[x][y]+1 # 방의 색을 바꿔줘야하니깐 +1해주는것.

print(bfs((0,0)))