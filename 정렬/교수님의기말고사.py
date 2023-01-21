n,m,s = map(int,input().split())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
arr.sort()
def solve():
    for i in range(0,n-1):
        if arr[i + 1][0] - arr[i][0] - arr[i][1] >= m: # [i][1]은 경과시간임. 주의!
            return (arr[i][0] + arr[i][1]) # [i][1]은 경과시간임
def solve2():
    if arr[-1][0] + arr[-1][1] + m <= s:
        return arr[-1][0] + arr[-1][1]
if arr[0][0] >= m: # 0번째 시험이 시작하기 전에 시험을 진행하는 경우
    print(0) # 0에서부터 가능한경우
elif solve() != None: # 0~ n-1번째 시험 사이에 껴서 시험을 보는경
    print(solve())
elif solve2() != None: # 마지막 시험이 끝난 이후 시험을 보는 경우
    print(solve2())
else:
    print(-1)