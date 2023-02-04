import sys
import math
input = sys.stdin.readline

x ,  y = map(int, input().split(' '))

# total_x = x
# total_y = y

original_rate = math.trunc(y/x*100)


'''
앞으로 모든 게임 다이긴다
'''

start = 1
end = x # 얼만큼 상한선을 줘야할까 -> x만큼 이기면 오르지 않을까

res= -1

while start<=end:
    mid = (start+end)//2

    total_x = x+ mid
    total_y = y+mid

    change_rate = math.trunc(total_y/total_x*100)

    if change_rate>original_rate: # 값이 변하면
        res= mid
        end = mid-1 # 이미 충분히 컸으니까 줄여
    else:
        start = mid+1 # 부족하면 더 더해

print(res)