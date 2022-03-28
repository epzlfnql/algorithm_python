# 거스름돈 개수가 가장 적게
import sys

mon = 1000
rest = [500, 100, 50, 10, 5, 1] # 거스름돈

input = int(sys.stdin.readline())

rest_money = mon - input
count = 0
for i in rest:
    if(rest_money<=0):
        break
    else:
        count += rest_money//i
        rest_money = rest_money % i


print(count)