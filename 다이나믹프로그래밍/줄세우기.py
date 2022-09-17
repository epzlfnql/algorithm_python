'''
옮겨지는 아이의 수가 적게끔
일렬로
'''

import sys
input = sys.stdin.readline

n = int(input()) # 아이수
arr = list(int(input()) for _ in range(n))
# [3, 7, 5, 2, 6, 1, 4]

# 증가하는 부분 수열 구하고 전체길이에서 빼주기
dp =[1]*(n)
for i in range(n):
    max_len = 0
    for j in range(i):
        if arr[j]<arr[i] and max_len<dp[j]:
            max_len=dp[j]
            dp[i] = max_len+1

print(n - max(dp))