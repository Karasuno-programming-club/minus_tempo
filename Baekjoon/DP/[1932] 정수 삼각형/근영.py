N = int(input())
tri = [[0]]

for i in range(N):
    tri.append(list(map(int, input().split())))

if N == 1:
    print(tri[1][0])
    exit(0)

dp = [[0]]
for i in range(N):
    dp.append([0] * (i+1))

dp[1] = tri[1]

for i in range(2, N+1):
    for j in range(i):
        if j == 0 :
            dp[i][j] = tri[i][j] + dp[i-1][j]
        elif j == i-1:
            dp[i][j] = tri[i][j] + dp[i-1][j-1]
        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[-1]))

