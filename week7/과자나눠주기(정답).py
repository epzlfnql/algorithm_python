#  최대한 긴 과자를 나눠준다.
# M명의 조카, N개의 과자
# 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠줘야 한다.
# 조각으로 나눌 수는 있지만 합칠수는 없다.

import sys
input = sys.stdin.readline


M ,N = map(int, input().split())

snack_length = list(map(int, input().split()))

#snack_length.sort() # 이진탐색을 위한 정렬 -> 이거 쓰면 시간초과 난다.

start = 0
end = max(snack_length) # 과자를 합칠수는 없으니까 가장 긴것으로 설정


k = 0
while start<=end:
    mid = (start+end)//2
    cnt = 0

    # 이 부분은 몰라서 참고한 부분
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을때
    if mid ==0:
        cnt = 0
        break

    for i in snack_length:
        if mid<=i:
            cnt+=(i//mid)



    # 이 부분을 바꾸지 않으면 답이 안나오는데 빠진 조건이 있는지;
    if cnt >=M:
        start = mid+1
        k = mid
    else:
        end = mid-1


print(k)

