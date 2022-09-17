import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 10, 20, 10, 30, 20, 50


dp = [1]*n #
for i in range(n):
    max_len = 0
    for j in range(i):
        #print(i, j)
        if arr[j]<arr[i] and max_len<dp[j]: #
            max_len = dp[j]
            dp[i]=max_len+1

print(max(dp))

