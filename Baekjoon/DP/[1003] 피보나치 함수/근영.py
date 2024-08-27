T = int(input())

def fibo(n):
    if(memo[n]):
        return memo[n]

    else :
        tempX = fibo(n-1)[0] + fibo(n-2)[0]
        tempY = fibo(n-1)[1] + fibo(n-2)[1]
        memo[n] = [tempX, tempY]
        return [tempX, tempY]

for _ in range(T):
    N = int(input())

    if N == 0 : print(1, 0, end=" ")
    elif N == 1 : print(0, 1, end=" ")
    else :
        memo = [False] * (N+1)
        memo[0] = [1, 0]
        memo[1] = [0, 1]

        fibo(N)
        print(*memo[N], end=" ")