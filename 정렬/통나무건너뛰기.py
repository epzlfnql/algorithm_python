import sys
input  = sys.stdin.readline

'''
N개의 통나무를 원형으로 세워 놓고 뛰어 놀려고 한다.

'''

T = int(input())
for _ in range(T):
    n= int(input()) # 통나무 개수
    tmp = list(map(int, input().split()))
    tmp.sort()
    res = 0
    for i in range(2, n):
        res = max(res, abs(tmp[i] - tmp[i-2]))
    print(res)