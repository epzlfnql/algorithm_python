import sys
input = sys.stdin.readline

# 강을 가로지르는 하나의 차선
# n개의 트럭
# 트럭의 순서는 바꿀 수 없고
# 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

n, w, l = map(int, input().split()) # 트럭의 수, 다리 길이, 다리의 최대 하중
weight = list(map(int, input().split()))# 트럭의 무게
print(weight)

res = 0
bridge_sum=[0]*w # 현재 다리에 올라와있는 트럭 무게들을 반환하기 위해

while bridge_sum:
    res+=1 # 시간
    bridge_sum.pop(0) # 다리위에 있는 트럭의 앞쪽이 나간것을 의미
    if weight:
        if (sum(bridge_sum) + weight[0])<=l:
            bridge_sum.append(weight.pop(0))
        else:
            bridge_sum.append(0)
print(res)