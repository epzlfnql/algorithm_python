import sys
'''
자연수가 쓰여진 카드 n장
i번 카드에 ai가 쓰여있다.
카드 합체 놀이는 이 카드들을 합체하며 노는 놀이

1. x번 카드와 y번 카드를 골라 그 두장에 쓰여진 수를 더한값을 계산
2. 계산한값을 x번 카드와 y번 카드 두장 모두에 덮어쓴다.

이 카드 합체를 총 m번 하면 놀이가 끝난다.
m번의 합체 이후, n장의 카드에 쓰여 있는 수를 모두 더한 값이 이 놀이의 점수가 된다.
-> 이 점수를 가장 작게 만드는 것이 놀이의 목표.
'''
input = sys.stdin.readline
n, m = map(int,input().split()) # n은 카드의 개수, m은 합체 횟수
card_list = list(map(int, input().split()))


for i in range(m):
    card_list.sort()
    tmp =  card_list[0] + card_list[1]
    card_list[0] = tmp
    card_list[1] = tmp

print(sum(card_list))


