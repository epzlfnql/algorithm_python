import sys


# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 정점의 개수,

edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))  # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

edges.sort()  # 비용으로 오름차순 정렬

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(연결시킨다.)
    if find(parent, a) != find(parent, b):  # 부모 노드가 다르다면
        union(parent, a, b)
        result += cost

print(result)