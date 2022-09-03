# 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램 작성 문제
# 2-친구는 두사람이 친구이거나 C인 친구를 건너 친구인 경우
# 가장 유명한 사람은 2-친구의 수가 가장 많은 사람

# N의 최대값이 50 이므로 플로이드 워셜 써도 될거같다..?
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())# 사람의 수
graph = []
for _ in range(N):
    tmp = list(map(str, input().strip()))
    graph.append(tmp)

two_friend = [[0]*N for _ in range(N)]





for a in range(N):
    for b in range(N):
        for k in range(N):
            if a==b: # 자기 자신일 경우 그냥 넘긴다. 이 부분 코드 안넣어서 계속 틀렸음..
                continue
            else:

                if graph[a][b]=='Y':
                    two_friend[a][b] = 1
                else:
                    if graph[a][k]=='Y' and graph[k][b]=='Y':
                        two_friend[a][b]=1

answer = 0
for t in two_friend:
    answer = max(answer, sum(t))

print(answer)