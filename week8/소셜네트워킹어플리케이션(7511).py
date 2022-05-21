
# 두 사람 사이에 경로가 존재하는지 안하는지를 미리 구해보려고 한다.
# 주어지는 두 사람이 친구 관계 그래프상에서 경로가 존재하는지 안하는지를 구하는 프로그램 작성


# union 하고 find하면 될듯?

import sys
input = sys.stdin.readline


# find함수
def find_parent(parent, x):
    if parent[x]!= x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 함수
def union_parent(parent, a, b):
    a= find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] =a
    else:
        parent[a] = b



T = int(input())# 테스트 케이스 수




for t in range(T):
    print("Scenario "+str(t+1)+":")
    result = []
    n = int(input()) # 유저의 수
    k = int(input()) # 친구 관계의 수

    # parent 선언
    parent = [0]*(n+1)
    for i in range(1, n+1):
        parent[i] = i

    for j in range(k):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 미리 구할 쌍의 수
    m = int(input())

    for h in range(m):
        u, v = map(int, input().split())
        if find_parent(parent, u)==find_parent(parent, v):
            print(1)
        else:
            print(0)
    print()
