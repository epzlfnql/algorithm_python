'''
시작시간, 끝나는시간
회의가 겹치지 않게 하면서 회의실을 사용할수 있는 최대 개수
'''

import sys
input = sys.stdin.readline

n = int(input()) # 회의의 개수

time_list = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    time_list.append([a,b])


time_list.sort()# 끝나는 시간이 똑같을 경우 앞에 있는것이 빠른것을 먼저 고려
time_list.sort(key=lambda x: x[1]) # 끝나는 시간을 기준으로 정렬

print(time_list)

# 맨처음에 있는건 무조건 들어간다. -> 끝나는 시간이 가장 빠르므로
start = time_list[0]
cnt=1


for i in range(1, len(time_list)):
    if time_list[i][0]>=start[1]: # 다음시간의 시작시간이 이전시간의 끝나는 시간보다 크거나 같으면
        cnt+=1
        start = time_list[i]
print(cnt)

