import sys
input = sys.stdin.readline

n = int(input())

tmp = list(map(int, input().split()))
tmp_set = list(sorted(set(tmp)))



dic = {tmp_set[i]:i for i in range (len(tmp_set))}

for i in tmp:
  print(dic[i],end=' ')
