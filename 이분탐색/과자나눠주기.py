'''
막대과자 하나씩 나눠준다
최대한 긴 과자를 나눠주려고 한다
모든 조카에게 똑같은 길이의 막대 과자

막대 과자는 여러조각으로 나눠질수 있지만 하나로 합칠 수 없다
-> 쪼개는건 가능한데 합칠수는 없다.

'''
import sys
input = sys.stdin.readline

m, n = map(int, input().split(' ')) # 조카의 수, 과자의 수
snack_len = list(map(int, input().split(' ')))

snack_len.sort()

# 일단 그냥 해볼까
start = 0
end = snack_len[-1]

res = 0
res_list = []
while start<=end:
    mid =(start+end)//2

    # 개수 반환하는거 구해볼까
    cnt = 0
    for i in snack_len:
        cnt+=(i//mid)



    # 너무 많으면 -> mid 크기를 키워야한다
    if cnt>= m:
        res_list.append(mid)
        start = mid+1

    # 너무 없으면 -> mid 크기를 줄여야한다.
    else:
        end = mid-1


if len(res_list)!=0:
    print(max(res_list))
else:
    print(0)




'''

---- 정답코드 ----
근데 모든 조카에게 같은 길이의 막대과자를 나눠줄수 없을때 부분이 이해되지 않는다.
왜 mid==0일때만 고려하는지

import sys

# 조카의 수, 과자의 수
m, n = map(int, sys.stdin.readline().split())
# 과자의 길이
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때
    if mid == 0:
        total = 0
        break
    
    for x in arr:
        if x >= mid:
            total += (x//mid)

    if total >= m:
        start = mid + 1
        result = mid
        
    else:
        end = mid - 1

print(result)
'''