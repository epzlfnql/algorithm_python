import sys
input = sys.stdin.readline
from bisect import bisect_left
'''
정확히 3명으로 구성된 팀만 참가 가능
세팀원의 코딩 실력의 합이 0이 되는 팀을 만들어야한다.
만들 수 있는 경우의 수
'''


n = int(input()) # 학생의 수
a_list = list(map(int, input().split()))# 코딩 실력
a_list.sort()


result = 0 # 합이 0으로 만들 수 있는 경우의 수
for i in range(len(a_list)-2):
    l, r = i+1, n-1 # i를 기준으로 이후에 2개의 index를 선정
    while l<r:
        tmp_sum = a_list[i]+a_list[l]+a_list[r]
        if tmp_sum>0:
            r-=1
        else:
            if tmp_sum==0:
                # left와 right 똑같은 값이 나올 경우
                if a_list[r] == a_list[l]:
                    result+= (r-l)
                else: # 이해가 잘 안되는데 오른쪽에 있는애가 중복값이 있는경우 고려?
                        # 일단 a_list[r]!= a_list[l] 일때
                    idx = bisect_left(a_list, a_list[r]) # 인덱스 반환함수
                    result+= r -idx +1
            l+=1

print(result)
