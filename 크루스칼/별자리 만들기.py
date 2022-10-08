import sys
input = sys.stdin.readline
import math
n = int(input()) # 별자리 만들기

# 두별 사이의 거리(cost) 구하기
def find_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# 부모 테이블 초기화
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

tmp = []
for _ in range(n):
    a, b= map(float, input().split())
    tmp.append((a,b))


edges = []
total_cost = 0



# 거리(cost), 노드 이름, 노드이름 저장.
for i in range(n-1):
    for j in range(i+1, n):
        cost = find_distance(tmp[i], tmp[j])
        edges.append((cost, i, j))



# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()


# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in edges:
    cost, a, b = i

    # find 연산 후, 부모노드 다르면 사이클 발생x이므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost +=cost

print(round(total_cost,2))