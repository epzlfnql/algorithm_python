import sys
input = sys.stdin.readline

n = int(input()) # 수열 크기

a_list = list(map(int, input().split(' ')))
# print(a_list)
'''
a1, a2, a3, a4, a5, a6
3   3   1   1   4   4
i < j <= N    //  ai != aj중 j 최소값 
'''
result_list = [-1]*(n)

start_idx=0
base_num = a_list[0]
for i in range(1, len(a_list)):


    if a_list[i]==base_num:
        continue
    else: # 이전값이랑 달라지면
        # print(result_list[start_idx:i])
        result_list[start_idx:i]=[i+1]*(i-start_idx) # start_idx ~ i범위까지 i+1값 넣어주기
        base_num = a_list[i] # 새롭게 갱신
        start_idx = i

for num in result_list:
    print(num, end= ' ')