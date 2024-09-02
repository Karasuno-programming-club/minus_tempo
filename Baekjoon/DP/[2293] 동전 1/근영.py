N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for c in coins:
    for j in range(c, K+1):
        dp[j] = dp[j] + dp[j - c]

print(dp[K])

# 어렵당