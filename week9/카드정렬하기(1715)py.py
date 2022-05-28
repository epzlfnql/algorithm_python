# 정렬된 두 묶음의 숫자 카드
from queue import PriorityQueue
import sys
input = sys.stdin.readline
q = PriorityQueue()
n = int(input()) # 카드 묶음의 개수



for _ in range(n):
    tmp = int(input())
    q.put(tmp)

result = 0

while q:
    if q.qsize()<=1:
        break
    else:
        a =q.get()
        b =q.get()
        tmp =a+b
        result+=tmp
        q.put(tmp)

print(result)


