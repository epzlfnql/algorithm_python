# 시간 제한 2초, dp 사용하는 문제인지 일단 확인

import sys
input = sys.stdin.readline
INF = int(1e9)

N, D = map(int, input().split()) # 지름길의 개수, 고속도로의 길이

# 지름길 정보
cross_road = []
for _ in range(N):
    a,b,c = map(int, input().split()) # 출발지점, 도착지점, 지름길의 길이
    if b<=D: # 역주행은 안되므로 도착지점이 고속도로 길이를 넘지 않을 경우만 넣어준다.
        if b-a>c: #지름길의 길이가 더 짧을 때만
            cross_road.append([a,b,c])
    else:
        continue

dp = [0]*(D+1)

#print(len(dp))


#print(cross_road)

for i in range(1, D+1):
    dp[i] = dp[i-1]+1


    for a, b, c in cross_road:
        if b==i:
            dp[i] = min(dp[i-1]+1, dp[a]+c, dp[i])

print(dp[D])
