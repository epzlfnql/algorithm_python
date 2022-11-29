import sys
input = sys.stdin.readline
n, m = map(int,input().split()) # n 책의 개수, m 한번에 들수 있는 책의 개수


idx = list(map(int, input().split()))

idx.sort()
minus_list = []
plus_list = []
for i in idx:
    if i<0:
        minus_list.append(i)
    else:
        plus_list.append(i)

print(minus_list)
print(plus_list)

# 양수, 음수 절댓값 중 어떤게 더 큰지 확인
 # 음수의 절대값이 더 클때 -> 양수먼저 돌린다

plus_tmp = len(plus_list) % m  # 나머지 구해주기
plus_tmp2 = len(plus_list) // m  # 몫 구해주기

minus_tmp = len(minus_list) % m  # 나머지 구해주기
minus_tmp2 = len(minus_list) // m  # 몫 구해주기


res = 0

# 양수 연산 먼저

if abs(minus_list[0]) > abs(plus_list[-1]): # 각자 끝범위의 절대값 비교 -> 음수가 더크면 양수먼저 돌린다.


    # plus_res = []
    res += plus_list[plus_tmp-1]*2
    for i in range(1, plus_tmp2):
        print(plus_list[i*m]-1)


# 다시 돌아오는게 더 낮은거를 먼저 처리
# [-39, -37, -29, -28, -6, 2, 11]
# 2 + 9 + 11 + 6 +6 + 28+ 1+ 29 + 37 + 2
print(2 + 9 + 11 + 6 + 6 + 28+ 1+ 29 + 37 + 2)


# 양수방향 음수방향 따로 지정해야하는지?
# [-45, -26, -18, -9, -4, 22, 40, 50]
# 더 먼것을 나중에 한다.(돌아올때 힘드니까냬
# 이번엔 음수 먼저
# 4+5 +9+18+8+19 + 45 + 22+ 18+ 10
print(4+5 +9+18+8+19 + 45 + 22+ 18+ 10)