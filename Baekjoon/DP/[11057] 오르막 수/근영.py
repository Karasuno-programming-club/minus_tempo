N = int(input())

dp = [[1 for _ in range(10)] for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(10):
        if j == 0 :
            dp[i][j] = 1
        else :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1] % 10007)