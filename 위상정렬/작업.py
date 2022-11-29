'''
수행해야할 작업 n개
선행 관계에 있는 작업들의 번호는 모두 1이상 (k-1_이하
선행 관계에 있는 작업이 하나도 없는 작업이 반드시 하나이상 존재
서로 선행 관계가 없는 작업들은 동시에 수행 가능

'''

import sys
from collections import deque
input = sys.stdin.readline
dQ = deque()
n = int(input())


result = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
cost_list = []


for i in range(0, n):
    tmp = list(map(int, input().split()))

    cost = tmp[0]
    cost_list.append(cost)
    #print(tmp)
    if tmp[1]==0:
        continue
    else:
        for j in range(tmp[1]):
            graph[i][tmp[j+2]]=1
            degree[i]+=1


for i in range(n):
    if degree[i]==0: # 차수가 0이면, 선행해야할 작업이 없으니까 큐에 넣는다.
        dQ.append(i)


# index 0 은 1번 노드 의미
#print(dQ)


while dQ: # 큐가 빌때까지
    x = dQ.popleft()
    # print(x, end=' ')

    for i in range(1, n+1):
        if graph[i][x+1]==1: # x에 도착하는게 있으면
            degree[i]-=1
            result[i] = result[x+1]+cost_list[i]

            if degree[i]==0:
                dQ.append(i)

# print(cost_list)
print(result[n-1])
# print(result)
# #
# # print(graph)
# # print(degree)

