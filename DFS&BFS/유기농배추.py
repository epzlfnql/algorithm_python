from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for q in range(4):
            nx = x+dx[q]
            ny = y+dy[q]
            if nx<0 or ny<0 or  nx>n-1 or ny>m-1:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                que.append((nx, ny))



for _ in range(t):
    m, n, k = map(int, input().split(' '))
    ans = 0

    graph = [[0]*m for i in range(n)]
    # visited = [[0]*m for i in range(n)]

    # graph 채워주고
    for s in range(k):
        x, y = map(int, input().split(' '))
        graph[y][x]=1 # 이거 헷갈릴만함


    for a in range(n):
        for b in range(m):
            if graph[a][b]==1:
                bfs(a, b)
                ans+=1

    print(ans)
    # print(graph)
    # print()