N = int(input())

hi = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range (1, 101):
        if j <= hi[i-1] :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - hi[i-1]] + happy[i-1])

print(dp[-1][-1])