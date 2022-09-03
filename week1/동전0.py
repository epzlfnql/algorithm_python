import sys
input = sys.stdin.readline

N, K = map(int, input().split())

tmp = []
for i in range(N):
    tmp.append(int(input()))


count = 0

tmp.sort(reverse=True)



for i in tmp:
    if(K<=0):
        break

    else:
        if(K>=i):

            temp2 = K//i #몫
            count+=K//i
            K = K-temp2*i
        else:
            continue

print(count)