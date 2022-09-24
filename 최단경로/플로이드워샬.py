import sys
input = sys.stdin.readline

'''
그래프에서 모든 정점에서 모든 정점으로 가는 최단 거리를 구하는것.
dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]
'''

n, m = map(int, input().split()) # 정점번호, 간선 개수
dis = [[5000]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dis[i][i]=0

for i in range(m):
    a,b,c = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j]==5000:
            print('M', end = ' ')
        else:
            print(dis[i][j], end = ' ')
    print()
