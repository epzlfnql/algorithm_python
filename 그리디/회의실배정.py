'''
그리디 -> 정렬과 동반된다.
'''
import sys
n = int(input()) # 회의의 개수
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

et = 0
cnt = 0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1