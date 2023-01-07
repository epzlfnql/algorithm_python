'''
수가 적혀 있는 p1~ pn개 카드
1부터 n까지 수가 하나씩 존재하는 D1, D2, ... Dn가 있다.


'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split(' ')) # 카드 개수, 카드 섞은 횟수
after_k = list(map(int, input().split(' '))) # k번 카드를 섞은 후 카드 배치
d = list(map(int, input().split(' '))) # 카드 가져오는 순서

tmp_list = after_k # 계속 갱신해줄거다.



for i in range(k):

    res = [0] * n  # 너무 화나는데 이렇게 안에 안넣어주면 tmp_list가 이상하게 갱신된다..


    for num, j in enumerate(d):

        res[j-1] = tmp_list[num]
    #     print(tmp_list[num])
    # print()


    # print(res)
    tmp_list = res
    # print()


for i in res:
    print(i, end= ' ')