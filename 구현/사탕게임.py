import sys
input = sys.stdin.readline

# 봄보니 게임
# 사탕의 색은 모두 같지 않을 수 있다.
# 사탕의 색이 다른 인접한 두 칸을 고른다.
# 고른 칸에 들어있는 사탕을 서로 교환한다.
# 사탕의 위치 교환?
# 모두 같은 색으로 이루어져있는 가장 긴 연석 부분을 모두 먹는다.

n = int(input()) # 보드의 크기

board = [] # 색상정보 저장을 위해
for _ in range(n):
    colors = list(map(str, input()))
    board.append(colors)

maxCount = 0  # 최대 사탕 개수를 초기화

# 배열의 행 마다 같은 색의 사탕이 몇개 있는지 계산
def width():
    global maxCount
    for k in range(n): # 행을 돌면서
        countRow = 1  # 초기 개수를 1로 초기화
        for l in range(n - 1): # 앞에서 이미 1로 초기화 해줬기 때문에 n-1만큼만 돈다. 그리고 index out of range 안나게 하기 위해
            if board[k][l]== board[k][l + 1]:  # 만약 같은 열의 사탕의 색이 같다면
                countRow += 1  # 사탕 개수 1 증가
                maxCount = max(maxCount, countRow)  # 증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else:  # 만약 같은 열의 사탕 개수가 다르다면
                countRow = 1  # 개수를 1로 초기화


# 배열의 열마다 같은 색의 사탕이 몇개 있는지 계산
def height():
    for k in range(n):
        global maxCount

        countColumn = 1  # 초기 개수를 1로 초기화
        for l in range(n - 1):
            if board[l][k] == board[l + 1][k]:  # 만약 같은 행의 사탕의 색이 같다면
                countColumn += 1  # 사탕 개수를 1개씩 증가시켜주고
                maxCount = max(maxCount, countColumn)  # 증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else:  # 만약 같은 행의 색이 다르다면
                countColumn = 1  # 개수를 1로 초기화


for i in range(n):
    for j in range(n - 1):
        # 만약 입력 받은 배열의 행의 원소가 다르다면
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            width()
            height()
            board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]
        # 만약 입력 받은 배열의 열의 원소가 다르다면
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
            width()
            height()
            board[j + 1][i], board[j][i] = board[j][i], board[j + 1][i]

print(maxCount)  # 색이 같은 사탕개수 최대값을 출력