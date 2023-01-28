import sys
import math
input = sys.stdin.readline

'''

'''
x,y,c = map(float, input().split())

start = 1
end = min(x,y) # 대각선의 길이보다는 빌딩 사이의 너비가 무조건 작다.
result = 0
while start<= end:
    tmp_len = (start+end)/2

    # w를 이용해서 c 계산
    h1 = math.sqrt(x**2-tmp_len**2)
    h2 = math.sqrt(y**2-tmp_len**2)


    # 사다리꼴 공식에 의하면
    # (윗변 + 아랫변)*높이 /2


    # (h1+h2)*tmp_len/2 == tmp_len* tmp_c + (h2+ h1- 2*tmp_c)*tmp_len/2
    # (h1+h2)/2 == tmp_c+(h2+h1-2*tmp_c)/2
    # (h1+h2) == 2*tmp_c+(h2+h1-2*tmp_c)

    # (h1+h2)*tmp_len/2 == h1*tmp_len/2 + tmp_c*tmp_len/2 +

    # 닮음비
    # a+b = tmp_len
    # a:tmp_c = tmp_len:h2
    # b:tmp_c = tmp_len:h1
    # tmp_c * tmp_len = h1*b
    # tmp_c * tmp_len = h2*a

    # tmp_len = a+b
    # tmp_len = tmp_c*tmp_len/h2 + tmp_c*tmp_len/h1
    # 1 = tmp_c /h2 + tmp_c/h1
    # 1 = (h1+h2) * tmp_c / h1*h2
    # tmp_c = (h1*h2)/(h1+h2)
    tmp_c = (h1*h2)/(h1+h2)
    if tmp_c>=c:
        result = tmp_len
        start = tmp_len+0.001 # 폭이 더 커야 한다.
    else:
        end = tmp_len-0.001

print(result)


