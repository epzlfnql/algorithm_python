# 앞에 있는 사람한테 우선으로 빌려주는게 좋을듯..?
def solution(n, lost, reserve):
    answer = 0
    tmp = [1]*n

    # 체육복 도난당한친구 1 빼주기
    for i in lost: # 0이 아니라 1번부터 있으니까
        tmp[i-1] = tmp[i-1]-1

    # 여벌 체육복 가져온친구 +1 해주기
    for i in reserve:
        tmp[i-1] = tmp[i-1]+1

    for i in range(len(tmp)):
        if(tmp[i]==2):# 여벌 체육복이 있는 경우
            if(i==0): # 가장 처음 인덱스일 때
                if(tmp[i+1]==0):
                    tmp[i+1]+=1
                    tmp[i]-=1

            elif(i==n-1): # 제일 끝 index일 때
                if(tmp[i-1]==0):
                    tmp[i-1]+=1
                    tmp[i]-=1

            else:
                if(tmp[i-1]==0): # 앞에 먼저 처리
                    tmp[i-1]+=1
                    tmp[i]-=1
                elif(tmp[i+1]==0):
                    tmp[i+1]+=1
                    tmp[i]-=1
                else:
                    continue


    for i in tmp:
        if(i>=1):
            answer+=1
    return answer

