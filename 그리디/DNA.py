import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tmp = [['temp']*m for _ in range(n)]


input_list = []
for i in range(n):
    input_list.append(list(input().rstrip()))



# 기존 2차원 배열을 세로로 zip할수 있는 방법
tranpose_rowcol = list(zip(*input_list))


dna = ''
result = 0

# print(tranpose_rowcol)

for a in tranpose_rowcol:
    # print(a)
    # print(n)
    max_value = 0
    max_element = 0
    # 값의 개수가 중복될 경우 사전순으로

    b = sorted(list(a), reverse=True)
    # print(b)
    for i in b:
        # print(i)
        if a.count(i) >= max_value:
            max_element, max_value = i, a.count(i)

    dna +=max_element
    result= result+(n-max_value)

print(dna)
print(result)



