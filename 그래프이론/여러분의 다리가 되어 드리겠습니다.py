import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x]!= x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n = int(input())

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i]=i


for _ in range(n-2):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


# 임시로 부모노드값 저장하기 위해
tmp = []
for i in range(1, n+1):
    tmp.append(find_parent(parent, i))

tmp2 = list(set(tmp))
print(tmp2[0], tmp2[1])

