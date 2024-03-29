'''
돌 게임 - 두명이서 즐기는
돌  N개
- 상근이와 창영이는 턴을 번갈아가면서 돌을 가져간다.
- 돌은 1, 3, 4개 가져갈 수 있다.
마지막 돌을 가져가는 사람이 게임 이긴다.
두 사람이 완벽하게 게임 진행
게임은 상근이가 먼저 시작
'''

import sys
input = sys.stdin.readline

n = int(input()) # 돌 개수


dp = [0] * 1001

# 남은 돌이 1, 3, 4 이고 내 차례라면 무조건 이긴다.
# 남은돌이 2개면 무조건 진다. (딱 나눠 떨어져야하므로)

dp[1] = 'w'
dp[2] = 'l'
dp[3] = 'w'
dp[4] = 'w'

for i in range(5, n+1):
    if 'l' in (dp[i-1], dp[i-3], dp[i-4]): #  1,3,4개만 뽑을 수 있으므로  -> 5개의 경우 2개만 남겨서 상대를 패배시킬 수 있다. -> 그럼 내가 이긴다.
        dp[i] = 'w'
    else:
        dp[i] = 'l' # 상대를 패배시킬 수단이 하나라도 없으면 내가 진다.

if dp[n]=='w':
    print('SK')
else:
    print('CY')
