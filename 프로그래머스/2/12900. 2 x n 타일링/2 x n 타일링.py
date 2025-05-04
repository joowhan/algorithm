def solution(n):
    answer = 0
    # 맨 마지막 1에는 세로 배치 경우밖에 없음
    # 맨 마지막 2에는 가로 2개, 세로 2개 총 2가지
    # 맨 마지막 3에는 총 2개
    # n=1 -> 1, n=2 -> 2, n=3 -> 3, n=4 -> 
    dp = [0 for _ in range(n)]
    dp[0]=1
    dp[1]=2
    for i in range(2, n):
        dp[i] = (dp[i-1]+dp[i-2])%1000000007
    answer = dp[n-1]%1000000007
    
    return answer