'''
계단에 오르면 쓰여있는 점수를 얻게된다.

1) 계단은 한번에 한계단씩 또는 두 계단씩 오를 수 있다.
2) 연속된 세 개의 계단을 모두 밟아서는 안된다.
3) 마지막 도착 계단은 반드시 밟아야 한다.

'''
import sys
input = sys.stdin.readline

n = int(input()) # 계단의 수

tmp = []
for _ in range(n):
    tmp.append(int(input()))



dp = [0] * (n+1)

if n<=2:
    print(sum(tmp))
else:

    dp[0] = tmp[0]
    dp[1] = tmp[0]+tmp[1]
    dp[2] = max(tmp[0]+tmp[2], tmp[1]+tmp[2])
    for i in range(3, n):
       dp[i] = max(dp[i-2]+tmp[i], dp[i-3]+tmp[i]+tmp[i-1])

    # print(dp)
    print(dp[n-1])
