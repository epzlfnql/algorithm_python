import sys
input = sys.stdin.readline

n = int(input())
a =list(map(int, input().split()))
b =list(map(int, input().split()))


a.sort()
b.sort(reverse=True)

tmp = []

for i in range(n):
    tmp.append(a[i]*b[i])

print(sum(tmp))