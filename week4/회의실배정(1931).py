import sys
input = sys.stdin.readline



tmp = []
N = int(input())# 회의의 수
for _ in range(N):
     a,b = map(int, input().split())
     tmp.append([a,b])


tmp = sorted(tmp, key=lambda x:x[0]) # [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
tmp = sorted(tmp, key=lambda x:x[1])

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in tmp:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)



# 처음 sorted를 안하면 왜 틀리는지 모르겠다. --> 같은값이 나올수 있기 때문에(이해했음)
# 거꾸로 풀어보자 reverse true로