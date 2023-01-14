'''
부피 a,b,c
앞 두물통은 비어있고
세번째 물통은 가득
한 물통이 비거나
다른 한 물통이 가득찰때까지 물을 부을수 있다.
손실되는 물은 없다

아니 도대체 어떻게 1 2 8 9 10이 나오는거야
'''
from collections import deque
import sys
input = sys.stdin.readline

# 부피 범위
a,b,c = map(int, input().split(' ')) # 물통 용량

# 경우의 수를 담을 큐
que = deque()
que.append((0,0))

# 방문 여부(visited[x][y])
visited = [[False] * (b+1) for _ in range(a+1)] # a, b의 용량 여부에 따라 2차원 배열 생성
visited[0][0] = True

# 답을 저장할 배열
answer = []


# x, y의 경우의 수 저장
def pour(x, y):
    if not visited[x][y]: # 아직 방문하지 않았으면
        visited[x][y]=True
        que.append((x, y))



def bfs():

    while que:
        # x : a 물통의 물의 양, y : b물통의 물의 양, z : c물통의 물의 양
        x, y = que.popleft()
        z = c - x - y

        # a 물통이 비어있는 경우 c물통에 남아있는 양 저장
        if x==0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x-water, y+water)
        # x -> z
        water = min(x, c-z)
        pour(x-water, y)
        # y -> x
        water = min(y, a-x)
        pour(x+water, y-water)
        # y -> z
        water = min(y, c-z)
        # z -> x
        water = min(z, a-x)
        pour(x+water, y)
        # z -> y
        water = min(z, b-y)
        pour(x, y+water)

bfs()

answer.sort() # 오름차순 정렬
for i in answer:
    print(i, end= ' ')
