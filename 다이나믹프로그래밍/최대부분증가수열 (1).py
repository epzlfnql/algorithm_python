import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.insert(0,0) # 순서를 미루기 위해 , 1번부터 시작하게 하기 위해
dy = [0]*(n+1)
dy[1] = 1 # 직관적으로 1
res = 0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1): # 거꾸로
        if arr[j]<arr[i] and dy[j]>max: # 부분 증가수열이 되기 위해서는 i번째수가 마지막 항이 되어야함. 즉 번째 수가 i번째 수보다 작아야한다. 그리고 max(==최대길이) 갱신을 위해
            max = dy[j]
    dy[i] = max+1 #
    if dy[i]>res:
        res = dy[i]
print(res)