import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, x, y, M, N):

    dx = [0,0,-1,1]
    dy= [-1,1,0,0]
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for h in range(4):
            nx = x+dx[h]
            ny = y+dy[h]
            if nx<0 or ny<0 or  nx>N-1 or ny>M-1:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx, ny))
    return


T = int(input()) # 테스트 케이스 개수

for case in range(T):
    worm_num = 0
    N, M, K = map(int, input().split())
    graph = [[0]* M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for x in range(N):
        for y in range(M):
            if graph[x][y]==1:
                bfs(graph, x, y, M, N)
                worm_num+=1

    print(worm_num)


# 가로, 세로 인덱스 문제 때문에 오래걸렸다..