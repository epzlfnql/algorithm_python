import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x, y):
    que = deque()
    que.append([x,y])

    area = 1

    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]

            if 0<=nx <n and 0<=ny <m and graph[ny][nx]==0:
                graph[ny][nx]=1
                que.append([ny, nx])
                area+=1


    return area

graph = [[0]*n for _ in range(m)]

tmp =[]

for _ in range(k):
    tmp.append(list(map(int, input().split())))# x1, y1, x2, y2 입력받기


# 그래프 visit 해주기
for i in tmp:
    for x in range(i[1], i[3]):
        for y in range(i[0], i[2]):
            graph[x][y] = -1 # 색칠해주기



cnt=0 # 영역의 개수
result = []
for x in range(m):
    for y in range(n):
        if graph[x][y]==0:
            graph[x][y]=1
            tmp2 = bfs(x, y)
            result.append(tmp2)
            cnt+=1


result.sort()
print(cnt)
for area in result:
    print(area, end=' ')
