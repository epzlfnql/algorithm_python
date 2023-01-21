'''
가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
길이가 L인 테이프 무한개 보유
물을 막을때, 적어도 그 위치의 좌우 0.5만큼 간격 주기
필요한 테이프의 최소 개수 구하기
테이프 자를수 없고 겹쳐서 붙이는것 가능
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split(' ')) # 물이 새는 곳의 개수, 테이프 길이
leak = list(map(int, input().split(' '))) # 물이 새는 곳의 위치


leak.sort() # 오름차순 정렬

start = leak[0]-0.5 # 좌 0.5 여분 주기
cnt= 1 # 맨처음꺼는 카운트하고 시작하니깐

for i in range(1, len(leak)):
    if start + l >= leak[i]+0.5: # 오른쪽 끝에서 0.5 만큼 여분을 줘야한다.
      continue
    else:
      cnt+=1
      start = leak[i]-0.5 # start 지점 새롭게 갱신

print(cnt)
# 0.5는 어떻게 고려해야할까