N = int(input())

result = []

for _ in range(N): 
    K = int(input())

    dp = [[0] * 3 for _ in range(K)]

    # 위
    A = list(map(int, input().split()))
    # 아래
    B = list(map(int, input().split()))

    # 위의 스티커을 떼는 경우
    dp[0][0] = A[0]

    # 밑의 스티커을 떼는 경우
    dp[0][1] = B[0]

    # 스티커를 떼지 않는 경우
    dp[0][2] = 0
    

    # for i in range(1, K):
    #     isEven = i % 2 == 0 

    #     if isEven:     
    #         dp[i][0] = dp[i-1][0] + A[i]
    #         dp[i][1] = dp[i-1][1] + B[i]
    #         dp[i][2] = dp[i-1][2] + max(A[i], B[i])
    #     else: 
    #         dp[i][0] = dp[i-1][0] + B[i]
    #         dp[i][1] = dp[i-1][1] + A[i]
    #         dp[i][2] = max(dp[i-1][0], dp[i-1][1])

    for i in range(1, K):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + A[i]  # 위쪽 스티커를 선택한 경우
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + B[i]  # 아래쪽 스티커를 선택한 경우
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])  # 스티커를 떼지 않는 경우

    result.append(max(dp[-1]))

print(*result, sep="\n")

# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ죽어