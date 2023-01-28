'''
A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))# A, B의 수
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    a.sort()
    b.sort()

    cnt = 0

    for i in range(len(a)): # a한개씩 돌면서
        tmp_a = a[i]
        res_list = []
        start = 0
        end = len(b)-1

        while start<=end:
            mid = (start+end)//2

            if tmp_a > b[mid]: # 조건을 만족하면
                res_list.append(mid+1)
                start = mid+1
            else: # 조건을 만족못하면
                end = mid-1

        # res_list에서 가장 큰값 하나만 넣어주면된다.
        if len(res_list)==0: # 한개도 없으면 그냥 continue
            continue
        else:
            cnt+= max(res_list)

    print(cnt)