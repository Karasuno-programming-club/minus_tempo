def dp(N):

    if N == 1:
        return A[0]
    if N == 2:
        return A[0] + A[1]
    
    d[0] = A[0]
    d[1] = A[0] + A[1]

    for i in range(2, N):
        # 현재 계단은 >> 두 계단을 한 번에 오르거나, 연속으로 두 계단을 올랐을 때 점수를 고려
        d[i] = max(d[i-2] + A[i], d[i-3] + A[i-1] + A[i])

    return d[N-1]

T = int(input())

A = []

d = [0] * (T+1)

for _ in range(T):
    A.append(int(input()))


print(dp(T))

# 와우 이게 실버라고?