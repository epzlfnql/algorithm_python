import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))

num_lst = [i for i in range(2,n+1)]
del_lst = []
# print(num_lst)

while num_lst: # 안에 리스트가 다 비워질때까지
    base_num = num_lst.pop(0)
    del_lst.append(base_num)
    for i in num_lst:
        if i%base_num==0: # base_num의 배수면
            del_lst.append(i)
            num_lst.remove(i)

print(del_lst[k-1])

# 아직 지우지 않은 수 중 가장 작은 수를 찾는다.
