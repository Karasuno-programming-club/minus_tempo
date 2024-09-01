N = int(input())
drinks = []
for _ in range(N):
    drinks.append(int(input()))

dp = [0] * N
dp[0] = drinks[0]

if N > 1 :
    dp[1] = drinks[0] + drinks[1]
if N > 2 :
    dp[2] = max(drinks[1] + drinks[2], drinks[0] + drinks[2], dp[1])
if N > 3 : 
    for i in range(3, N):
        dp[i] = max(dp[i-3] + drinks[i-1] + drinks[i], dp[i-2] + drinks[i], dp[i-1])

print(dp[-1])

# 현재 포도주를 안마시는 경우의 수를 생각하자,,