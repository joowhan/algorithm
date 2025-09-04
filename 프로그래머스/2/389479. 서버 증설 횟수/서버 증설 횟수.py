# 매 시간 이용자 수 표시 => 
# m 이상일 때 서버 증설, n*m <= x < (n+1)*m
# 시간 지나면 끄기
def solution(players, m, k):
    answer = 0
    n = len(players)
    active = [0]*(n+k)
    for i, player in enumerate(players):
        need = player //m
        curr = need - active[i]
        if curr >0:
            answer += curr
            for j in range(i, i+k):
                active[j] += curr
    return answer