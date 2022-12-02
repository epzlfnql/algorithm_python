import sys
'''
배열에 있는 모든 수는 서로 다르다.
ㅇ녀속된 두개의 원소만 교환 가능
교환은 S번 이내로

'''

input = sys.stdin.readline

n = int(input()) #
num_list = list(map(int, input().split()))
s = int(input())

for i in range(0,s*2, 2):
    tmp = num_list[i]
    num_list[i] = num_list[i+1]
    num_list[i+1] = tmp

for i in num_list:
    print(i, end = ' ')