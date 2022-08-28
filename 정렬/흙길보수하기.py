# n개의 물웅덩이
# 길이 L짜리 널판지 충분히 갖고 있다.
# 모든 물웅덩이들을 덮기 위해 필요한 널빤지들 개수 구하기

import sys
input = sys.stdin.readline

n, l = map(int, input().split())

tmp = []
for _ in range(n):
    start, end = map(int, input().split())# 시작 위치, 끝 위치
    tmp.append([start, end])


tmp.sort() # [[1, 6], [8, 12], [13, 17]]

result = 0
start = 0 # 인덱스
for i in tmp:

    if start>i[0]:
        i[0] = start
    else:
        start = i[0]
    #print(start)
    len_tmp = i[1]-start
    cnt = len_tmp//l
    if len_tmp%l>0:
        cnt+=1
    result+=cnt

    start += cnt*l

print(result)
