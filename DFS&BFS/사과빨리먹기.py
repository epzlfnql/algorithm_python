'''
5*5 크기
사과가 1개 있는격자
장애물이 있는격자
빈칸으로 되어있는 격자
격자의 위치는 (r,c)로 표시
행 번호는 맨위 위치가 0
아래방향으로 1씩 증가

열번호는 맨 왼쪽 위치가 0이고 오른쪽으로 1씩 증가
맨 왼쪽 위 위치가 (0,0), 맨 아래 오른쪽 위치가(4,4)

학생이 지나간 칸은 장애물이 있는 칸으로 변경

현재위치(r,c)에서 사과 3개를 먹기 위한 최소 이동 횟수 출력
만약 현재위치에서 사과 3개를 먹을수 없는경우 -1 출력

'''
from collections import deque
import sys
input = sys.stdin.readline

graph =[]
for _ in range(5):
    graph.append(list(map(int, input().split(' '))))

r, c = map(int, input().split(' '))

visited = [[0]*5 for _ in range(5)]

dx = [0,0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0  # 사과 먹은횟수
total_move = 0 # 총 이동횟수

def bfs(x, y, graph, visited, cnt, total_move):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny < 0 or nx>=5 or ny>=5:
                continue # 다시 되돌아가

            if visited[nx][ny]==0 and graph[nx][ny]==1:
                cnt+=1
                total_move+=1


                # 사과 3개인 경우
                if cnt==3:

                    return total_move
                else:
                    visited[nx][ny] = 1
                    graph[nx][ny] = -1
                    que.append((nx, ny))

            elif visited[nx][ny]==0 and graph[nx][ny]==0:
                total_move+=1
                visited[nx][ny]=1
                graph[nx][ny]=-1
                que.append((nx, ny))

            else: # 방문을 이미 했거나 장애물이 있거나
                continue



res= bfs(r, c, graph, visited, cnt, total_move)

if res:
    print(res)
else:
    print(-1)
