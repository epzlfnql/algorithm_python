'''
f : 한눈금 앞
b : 한눈금 뒤
l : 왼쪽 90도 회전
r : 오른쪽 90도 회전
'''
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수







for _ in range(t):
    tmp = list(input().rstrip())

    x_list = []
    y_list = []

    # 가장 최대값 저장을 위해
    max_n = 0
    max_s = 0
    max_w = 0
    max_e = 0

    # 현재 위치값 저장을 위해
    now_x = 0
    now_y = 0


    # 현재 방향을 알려주기 위해
    now_direction ='n' # 처음은 북쪽 방향으로 먼저 시작

    # 다시 r, l 을 만날때까지 가장 긴 길이를 쓰면될거같다.
    while tmp:

        t = tmp.pop(0)

        # 현재 디렉션이 north일때!
        # print(f't: {t}, dir : {now_direction}')
        if now_direction =='n': # 북쪽 방향을 향하고
            if t == 'F': # 앞으로 전진이면
                now_y+=1
                y_list.append(now_y)
                if now_y>=max_n:
                    max_n = now_y
            elif t =='B': # 뒤로면
                now_y-=1
                y_list.append(now_y)
                if now_y<=max_s:
                    max_s = now_y

            # R이나 L이 나오면 방향을 바꿔준다.
            elif t=='R':# 오른쪽으로 90도 회전이면
                now_direction = 'e'
            else: # 왼쪽으로 90도 회전이면
                now_direction = 'w'

            continue


        # 현재 디렉션이 남쪽(South)일때
        if now_direction =='s': # 남쪽방향을 향하고
            if t =='F': # 앞으로 전진이면
                now_y-=1
                y_list.append(now_y)
                if now_y<=max_s:
                    max_s = now_y
            elif t=='B': # 뒤로 가는거면
                now_y+=1
                y_list.append(now_y)
                if now_y>=max_n:
                    max_n = now_y

            elif t=='R':
                now_direction = 'w' # 우리 기준에서는 서쪽으로 변경
            else:
                now_direction = 'e'

            continue

        # 현재 디렉션이 동쪽(East)일때
        if now_direction =='e': # 동쪽방향을 향하고
            if t=='F':
                now_x +=1
                x_list.append(now_x)
                if now_x>=max_e:
                    max_e = now_x
            elif t=='B':
                now_x -=1
                x_list.append(now_x)
                if now_x<=max_w:
                    max_w = now_x
            elif t=='R':
                now_direction = 's'
            else:
                now_direction ='n'

            continue

        # 현재 디렉션이 서쪽(West)일때
        if now_direction=='w': # 서쪽방향을 향하고
            if t=='F':
                now_x-=1
                x_list.append(now_x)
                if now_x<=max_w:
                    max_w = now_x
            elif t=='B':
                now_x +=1
                x_list.append(now_x)
                if now_x>=max_e:
                    max_e = now_x
            elif t=='R':
                now_direction = 'n'
            else:
                now_direction ='s'

            continue
    print((max_n+abs(max_s)) * (max_e+abs(max_w)))






