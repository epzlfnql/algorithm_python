'''
n개의 랜선
영식은 k개의 랜선 보유 - 길이가 제각각

박성원은 랜선을 모두 n개의 같은 길이의 랜선으로 만들고 싶었기 때문에 k개의 랜선을 잘라서 만든다.

n개보다 많이 만드는 것도 n개를 만드는 것에 포함

최대 랜선의 길이를 구하는 프로그램
'''

import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # k - 이미 갖고 있는 랜선의 개수, n - 필요한 랜선의 개수


k_len = []
for _ in range(k):
    k_len.append(int(input())) # 이거땜에 런타임 에러?


k_len.sort() # [457, 539, 743, 802]
l = 1 # 이거 0으로 설정하면 계속 런타임 에러 뜬다;; n=1, k=1, input=1의 경우 결과가 출력되지 않는다.
r = k_len[-1]



while l<=r:
    mid = (l+r)//2

    cnt=0
    for i in k_len:
        cnt+=(i//mid)

    if cnt <n: # mid가 더 작아야한다. -> r을 줄이기
        r=mid-1
    else:
        result = mid
        l = mid+1


print(result)

