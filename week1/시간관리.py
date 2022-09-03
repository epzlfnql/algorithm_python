import sys
input = sys.stdin.readline

N = int(input())# 하루에 해야할 일

# 오른쪽으로 당기면 될거같다..?

tmp = []



for i in range(N):
    T, S = map(int, input().split())
    tmp.append([T,S])


tmp.sort(key=lambda x:x[1])
tmp.append([0,0])
result = tmp[0][1] - tmp[0][0]
t_rest = 0

t_sum = tmp[0][1]

for i in range(N-1):
    t_sum = t_sum + tmp[i+1][0]
    if(t_sum<=tmp[i+1][1]):
        continue
    else:
        result +=tmp[i+1][1]-t_sum

if(result>=0):
    print(result)
else:
    print(-1)



