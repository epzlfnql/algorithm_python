import sys
input = sys.stdin.readline


n = int(input()) # 집의 수
tmp = []

for i in range(n):
    tmp.append(list(map(int, input().split(' '))))

# print(tmp)

'''
0, 1, 2 는 각각 빨강, 초록, 파랑을 의미
'''
for i in range(1, len(tmp)):
    tmp[i][0] = min(tmp[i - 1][1], tmp[i - 1][2]) + tmp[i][0] # 빨강으로 칠할때
    tmp[i][1] = min(tmp[i - 1][0], tmp[i - 1][2]) + tmp[i][1] # 초록으로 칠할때
    tmp[i][2] = min(tmp[i - 1][0], tmp[i - 1][1]) + tmp[i][2] # 파랑으로 칠할때
print(min(tmp[n - 1][0], tmp[n - 1][1], tmp[n - 1][2]))

