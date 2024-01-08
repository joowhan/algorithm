
def solution(storey):
    answer = 0
    # 각 자리 비교
    # 6~9 사이 수라면 더하는 것이 이득
    while storey:
        temp = storey % 10
        if 6<= temp <= 9:
            answer += 10-temp
            storey +=10
        # 0~4 사이 수라면 빼는 것이 이득
        elif temp <=4:
            answer += temp
        # 5일 경우 가운데 숫자이다. 다음 자리 수가 5보다 크면 더하는 것이 더 이득이고 아니라면 빼는 것이 이득이다.
        else:
            if (storey//10)%10 >=5:
                storey +=10
            answer += temp
        storey//=10    
    return answer