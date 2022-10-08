'''
신장 트리란
- 하나의 그래프가 있을 때, 모든 노드를 포함하면서 즉, 모든 노드들 간에 서로 연결은 되어있되
사이클이 존재하지 않는 '부분' 그래프.
원본 그래프인 graph에서 신장 트리를 만들 수 있는 경우의 수들 중 최소의 간선 비용을 들여서 만들 수 있는 신장트리를 최소 신장 트리라고 한다.

<크루스칼 알고리즘의 동작 과정>
1. 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서(오름차순)로 정렬
2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들간의 사이클을 발생시키는지 확인
3. 만약 사이클이 발생하지 않은 경우, 최소 신장 트리에 포함시키고 사이클이 발생한 경우, 최소 신장 트리에 포함시키지 않음
4. 1~3번의 과정을 모든 간선 정보에 대해 수행
'''
import sys

v = int(input()) # 컴퓨터 수
e = int(input()) # 간선의 수

# 부모 테이블 초기화
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i]=i

# find 연산
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = []
total_cost = 0

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]
    # find 연산 후, 부모노드 다르면 사이클 발생x이므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost +=cost

print(total_cost)