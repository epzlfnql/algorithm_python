import sys
input = sys.stdin.readline

n, h= map(int, input().split())
up = []
down = []
for i in range(n):
    if i%2==0: # 종유석
        up.append(int(input()))
    else: # 석순
        down.append(int(input()))

up.sort()
down.sort()
obstacle_cnt=[]


for i in range(1, h+1): # 높이에 변화를 주면서 count
    l, r = 0, len(down)-1
    down_cnt=0
    while l<=r:
        mid = (l+r)//2
        if down[mid]>=i:
            down_cnt = len(down)-mid
            r=mid-1
        else:
            l=mid+1

    up_cnt=0
    l, r = 0, len(up)-1
    while l<=r:
        mid = (l+r)//2
        if h-up[mid]<i:
            up_cnt = len(up)-mid
            r = mid-1
        else:
            l=mid+1
    obstacle_cnt.append(up_cnt+down_cnt)

result = min(obstacle_cnt)
cnt = obstacle_cnt.count(result)
print(result, cnt)