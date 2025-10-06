# 스티커를 뜯어 얻어낼 수 있는 최댓값은?
# 하나를 뜯으면 양 옆의 스티커는 이용할 수 없음
def solution(sticker):
    answer = 0
    # dp로 풀어야 한다. 
    n = len(sticker)
    if n==1:
        return sticker[0]
    
    def dp(s):
        if len(s)==1:
            return s[0]
        dp = [0]*(len(s))
        dp[0], dp[1] = s[0],max(s[0],s[1])
        for i in range(2, len(s)):
            dp[i] = max(dp[i-1], dp[i-2]+s[i])
        return dp[-1]
    
    case1 = dp(sticker[:-1])
    case2 = dp(sticker[1:])
    return max(case1, case2)