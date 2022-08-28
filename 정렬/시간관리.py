# 하루에 해야 할일 총 N개 (1 ~ N)
# Ti시간 걸리고 Si 시 내에 이 일을 처리해야 한다.
# 0시부터 활동 시작, 동시에 일 처리 x
# 최대한 늦잠
# 모두 마감시간 내에 처리하면서 최대한 늦게 일을 시작할 수 있는 시간이 몇시인지

import sys
input = sys.stdin.readline

n = int(input())# 일의 수

tmp = []
for _ in range(n):
    t, s = map(int, input().split())
    tmp.append([t,s])


# 거꾸로 정렬
c = sorted(tmp, key = lambda x : -x[1])
#print(c)   [[5, 20], [1, 16], [8, 14], [3, 5]]

start = c[0][1] # 가장 늦은 시간을 기준으로


for i in c:

    while start-i[0]>i[1]-i[0]:
        start-=1
    start-=i[0]

print(start if start>=0 else -1)


