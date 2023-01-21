'''
알고리즘 기말고사는 M분동안 쉬는시간 없이 볼 예정
0분부터 S분까지 사용가능
S는 무조건 M이상
다른 시험도 예정되어 있어서 겹치지 않는 시간을 잡아야한다
x1~y1분동안 진행

답은 나오는데
메모리초과 코드

'''
import sys
input = sys.stdin.readline

n, m, s = map(int, input().split(' '))

time_list = [0] * (s+1) # 일단 비어있는 시간은 0으로 표시
# 근데 이렇게 만들면 S만큼 배열 개수를 만드는거라 메모리 효율이 매우 안좋다.
# 그래서 메모리 초과가 뜬다.

for _ in range(n):
    a, b = map(int, input().split(' '))
    end = a+b # b분 경과후 끝나는 시간대
    time_list[a]=1
    time_list[end]=1

# print(time_list)

time_len = 0 # 경과시간
for i in range(len(time_list)):
    if time_list[i]==0: # 비어있는 시간대부터 스타트 / 사실은 그전꺼부터 시작인데 그전이 1이든 0이든 상관없음
        time_len +=1 # 경과시간 +1
        if time_len == m-1: # 시간이 딱 맞는다면
            print(i-m+1) # 초기 시작하는 시간대 뽑기
            break
    else: # 다른 강의로 채워져있는시간이라면 다시 리셋
        time_len =0


if time_len==0:
    print(-1)

