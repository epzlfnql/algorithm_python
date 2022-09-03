import sys
input = sys.stdin.readline

tmp = list(input().split('-'))



for i in range(len(tmp)):
    if('+' in tmp[i]):
        tmp2 = list(map(int, tmp[i].split('+')))
        tmp[i] = sum(tmp2)
    else:
        tmp[i] = int(tmp[i])

result = tmp[0]

for i in range(len(tmp)-1):
    result-=tmp[i+1]

print(result)
