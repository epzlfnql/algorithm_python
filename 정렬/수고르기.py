'''
n개의 정수
두 수를 골랐을 때(같은 수일수도 있다)
그 차이가 m이상이면서 제일 작은 경우를 구하는 프로그램
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort() # 오름차순 정렬

# min_res = arr[-1] # 일단 가장 큰값으로 초기화 ->> 값이 작아질수록 갱신할것이다.


res= []

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[j]-arr[i]>=m: # m이상 차이나면
            res.append(arr[j]-arr[i])
            break



print(min(res))
'''
pypy로 제출해야 시간초과가 안뜬다...
'''
