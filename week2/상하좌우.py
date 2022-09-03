import sys
input = sys.stdin.readline

N = int(input()) # 공간의 크기
direct = input().split()
x, y=1,1

# L,R,U,D 에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L', 'R', 'U', 'D']

# 이동계획을 하나씩 확인
for i in direct:
    # 이동 후 좌표 구하기
    for j in range(len(move_types)):
        if i ==move_types[j]:
            nx = x+dx[j]
            ny = y+dy[j]

    if nx<1 or ny<1 or nx>N or ny >N:
        continue
    else:
        x, y = nx, ny

print(x, y)