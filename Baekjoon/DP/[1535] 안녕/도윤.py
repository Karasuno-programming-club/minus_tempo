# health = 100

# 사람 수 
N = int(input())

A = [[0,0]]


cost = list(map(int, input().split()))

happy = list(map(int, input().split()))

for i in range(N):
    A.append([cost[i], happy[i]])

dp = [[0] * (101) for _ in range(N+1)]  

for i in range(1, N+1):
    for w in range(1, 100):
        if A[i][0] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(A[i][1] + dp[i-1][w - A[i][0]], dp[i-1][w])

print(dp[-1][-2])