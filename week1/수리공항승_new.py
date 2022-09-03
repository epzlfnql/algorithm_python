import sys
input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

print(arr)
start = arr[0]
ans = 1
for item in arr:
    if item>=start+L:
        ans+=1
        start=item
print(ans)