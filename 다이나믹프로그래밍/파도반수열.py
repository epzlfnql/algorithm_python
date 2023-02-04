import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수

t_list = []
for _ in range(t):
    t_list.append(int(input()))

dp = [0]*102

dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3

for i in range(5, 101):
    dp[i] = dp[i-5]+dp[i-1]


for j in t_list:
    print(dp[j-1])