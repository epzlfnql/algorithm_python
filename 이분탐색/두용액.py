# 산성 용액 알칼리성 용액
import sys
import math
input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))

tmp.sort() # -99 -2 -1 4 98
# 인덱스를 기준으로 ?
l = 0
r = len(tmp)-1

min_base = math.inf


while l<r:
    tmp_sum = tmp[l]+tmp[r]
    if abs(tmp_sum)<min_base:
        min_base = abs(tmp_sum)
        result_a, result_b = tmp[l], tmp[r]
    if tmp_sum==0:
        break
    if tmp_sum<0:
        l+=1
    else:
        r-=1


print(result_a, result_b)