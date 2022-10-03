import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a] = b







# 부모 테이블에서, 부모를 자기 자신으로 초기화
parent = [i for i in range(n+1)]

# cycle = False # 여행을 갈 수 있는지
#print(parent)

arr= []
for _ in range(n):
    arr.append(list(map(int, input().split())))

#print(arr)
for x in range(n):
    for y in range(n):

        if arr[x][y]==1:
            union_parent(parent, x+1, y+1)

final_path = list(map(int, input().split()))



# 경로 체크
root_num = find_parent(parent, final_path[1]) # 1씩 빼줘야한다.

#print(final_path)

#print(parent)
tmp = []
for i in final_path:
    tmp.append(parent[i])

set_tmp = set(tmp)
if len(set_tmp)>=2:
    print('NO')
else:
    print('YES')

