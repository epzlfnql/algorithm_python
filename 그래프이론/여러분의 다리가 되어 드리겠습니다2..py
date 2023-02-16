'''
n개의 섬
1,2, ...n의 번호가 하나씩 붙어있다.
그 섬들은 n-1개의 다리고 잇고 있다.
어떤 두 섬 사이든 다리로 왕복할 수 있었다.


욱제가 다리 하나 무너뜨림

'''

import sys
input = sys.stdin.readline
n = int(input()) # 섬 개수

# parent 배열 만들어주기
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x): # 이 부분만 이해가 안되네
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b= find_parent(parent, b)

    if a<b:
        parent[b] =a
    else:
        parent[a] =b


for _ in range(n-2):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

real_parent = []
for i in range(1, len(parent)): # 앞에 0은 빼줘야하니깐
    real_parent.append(find_parent(parent, parent[i]))

real_parent = set(real_parent)

for i in real_parent:
    print(i ,end= ' ')
