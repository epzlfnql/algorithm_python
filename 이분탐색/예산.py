'''
국가 예산 분배
총액은 미리 정해져있고

모든 요청이 배정될 수 있는 경우 요청한 금액 그대로 배정
모든 요청이 배정할 수 없는 경우 특정한 정수 상한액을 계산하여
그 이상인 예산요청에는 모두 상한액을 배정
상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정
'''

import sys
input = sys.stdin.readline

n = int(input())# 지방의 수
budget = list(map(int, input().split(' ')))
m = int(input()) # 예산


budget.sort() # 오름차순 정렬

start = 0
end = budget[-1]

result = 0

while start<=end:
    mid = (start+end)//2

    res= 0
    for i in budget:
        if i-mid >=0: # 예산이 부족하면
            res+=mid
        else:
            res+=i

    if res <=m:
        result = mid
        start = mid+1
    else:
        end = mid-1


print(result)