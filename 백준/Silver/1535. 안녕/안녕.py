n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
dp = [[0 for _ in range(100)] for _ in range(n+1)]
for i in range(1, n+1):
    joy, risk = J[i-1], L[i-1]
    for j in range(100):
        # 현재 체력보다 적으면? 
        if risk>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-risk]+joy, dp[i-1][j])
print(dp[n][99])