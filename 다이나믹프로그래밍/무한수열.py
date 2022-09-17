import sys
input = sys.stdin.readline
'''
탑다운 방식으로
'''

import sys

def dfs(num):
    global P, Q, arr
    if num < 1:
        return 1
    elif num in arr: # 이 부분이 살짝 이해안됨
        return arr[num]
    arr[num] = dfs(num//P) + dfs(num//Q)
    return arr[num]


if __name__ == "__main__":
    N, P, Q = map(int, sys.stdin.readline().split())
    arr = {}

    print(dfs(N))




# 시간 초과 코드
# # 딕셔너리 써보자
# n,p,q = map(int, input().split())
# dp = {}
# dp[0]=1
#
# def dfs(n):
#     if n<1:
#             return dp[n]
#     dp[n] = dfs(n // p) + dfs(n // q)
#     return dp[n]
#
# print(dfs(n))






# 메모리 초과
# n, p, q = map(int, input().split())
#
# dp = [0]*(n+1)
# dp[0] = 1
# def dfs(n):
#     if n==0:
#         return dp[n]
#
#     dp[n] = dfs(n//p)+dfs(n//q)
#     return dp[n]
#
# print(dfs(n))