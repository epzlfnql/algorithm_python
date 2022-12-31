import sys
input = sys.stdin.readline


n = int(input()) # 총 배달해야할거

# 5킬로그랭, 3킬로그램 봉지

cnt = 0
cnt_5 = n//5
cnt_3 = 0

while True:

    if cnt_5 ==-1:
        break

    res = n - cnt_5*5
    if res%3 ==0:
        cnt_3 = res//3
        print(cnt_5 + cnt_3)
        break
    else:
        cnt_5-=1






if cnt_5==-1:
    print(-1)
