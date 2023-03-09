import sys
input = sys.stdin.readline

n = int(input()) #

find_ans= int(input())
# (0,0)좌표에 n*n의 수가 들어간다.

nail_list = [[n*n]*n for _ in range(n)]
# print(nail_list)

vertical_cnt = n-1 # 1씩 줄여줄거다
horizon_cnt=n-1 # 1씩 줄여줄거다

vertical_total = -1 # 맨처음 시작할때 49는 고정되어있으므로 하나는 빼주고 드간다.
horizon_total = 0 # 2가 되면 0으로 갱신


i=0
j=0
dir = 'down'
while True:
    if nail_list[i][j]==1: # 1이 되면 그만하고 나오기
        break

    if dir=='down': # 아래로 가는방향일때
        vertical_total+=1
        if vertical_total==2:
            vertical_cnt-=1
            vertical_total= 0 # 초기화 해주기
        while True:

            if i==vertical_cnt:
                dir = 'right' # 오른쪽방향으로 바꿔주고
                break
            i += 1
            nail_list[i][j] = nail_list[i-1][j]-1

    elif dir =='right':
        horizon_total+=1
        if horizon_total==2:
            horizon_cnt-=1
            horizon_total=0
        while True:

            if j==horizon_cnt:
                dir = 'up'
                break
            j += 1
            nail_list[i][j] = nail_list[i][j-1]-1

    elif dir =='up':
        vertical_total += 1
        if vertical_total == 2:
            vertical_cnt -= 1
            vertical_total = 0  # 초기화 해주기
        while True:
            if n-i-1 == vertical_cnt:
                dir = 'left'  # 오른쪽방향으로 바꿔주고
                break
            i -= 1
            nail_list[i][j] = nail_list[i + 1][j] - 1

    else:
    # if dir =='left':
        horizon_total+=1
        if horizon_total==2:
            horizon_cnt-=1
            horizon_total=0
        while True:
            if n-j-1==horizon_cnt:
                dir = 'down'
                break
            j-=1
            nail_list[i][j] = nail_list[i][j+1]-1




for x in range(n):

    for y in range(n):
        if nail_list[x][y] ==find_ans:
            ans_x = x+1
            ans_y =y+1
        print(nail_list[x][y], end= ' ')

    print()


print(ans_x, ans_y)
