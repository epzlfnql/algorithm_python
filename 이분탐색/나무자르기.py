'''
나무 m미터 필요
절단기에 높이 h를 지정
적어도 m미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값 구하기
'''


import sys
input = sys.stdin.readline

n, m  = map(int, input().split()) # 나무의 수 n, 나무의 길이 m
h = list(map(int, input().split())) # 나무의 높이


h.sort() # 오름차순 정렬 [10, 15, 17, 20]
l = 0
r = h[-1]

# print(h)
# print(h[-1])

while l<=r:
    mid = (l+r)//2

    tmp = 0
    for i in h:
        if i>=mid:
            tmp+=(i-mid)


    # print(mid, tmp)
    if tmp<m:  # mid가 더 짧아져야한다.
        r = mid-1
    else:
        result = mid
        l= mid+1


print(result)
