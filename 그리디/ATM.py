# 1번부터 N번까지 번호
# p는 돈을 인출하는데 걸리는 시간

n = int(input()) # 사람의 수
time_use = list(map(int, input().split()))

time_use.sort()
# print(time_use)


result = 0
for i in range(len(time_use)):
    result+=sum(time_use[:i+1]) # 누적합

print(result)
