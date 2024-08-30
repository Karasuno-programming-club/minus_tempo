N, K = map(int, input().split())

things = [[0,0]]
for i in range(N):
       things.append(list(map(int, input().split())))

# 2차원 dp (x : 무게, y : 물건)
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if things[i][0] > j :
            dp[i][j] = dp[i-1][j]
        else: 
            dp[i][j] = max(dp[i-1][j - things[i][0]] + things[i][1] ,dp[i-1][j])

print(dp[-1][-1])