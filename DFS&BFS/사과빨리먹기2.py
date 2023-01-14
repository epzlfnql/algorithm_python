import sys
from collections import deque

input = sys.stdin.readline



graph =[]
for _ in range(5):
    graph.append(list(map(int, input().split(' '))))

r, c = map(int, input().split(' '))

visited = [[0]*5 for _ in range(5)]

dx = [0,0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0  # 사과 먹은횟수
total_move = [[0] * 5 for _ in range(5)]



def bfs(x, y, cnt):
    que = deque()
    que.append((x, y))

    # 큐가 빌 때까지 반복
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue

            # 벽인 경우 무시
            if graph[nx][ny]==-1:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1 or graph[nx][ny]==0:

                if graph[nx][ny]==1:
                    cnt+=1
                    if cnt==3:
                        return graph[x][y]+1

                graph[nx][ny] = graph[x][y]+1
                que.append((nx, ny))




res = bfs(r, c, cnt)
if res:
    print(res)
else:
    print(-1)
