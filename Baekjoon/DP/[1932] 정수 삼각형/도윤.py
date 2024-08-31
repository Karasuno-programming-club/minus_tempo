N = int(input())

A = [ [] for _ in range(N) ]


for i in range(N):
    A[i] = list(map(int, input().split()))


d = [[0] * N for _ in range(N)]

if N == 1:
    print(A[0][0])
    exit(0)


d[0][0] = A[0][0]

# 2번째 
d[1][0] = d[0][0] + A[1][0]
d[1][1] = d[0][0] + A[1][1]

# 배열의 첫 번째
for i in range(2, N): 

    for k in range(i+1):
        # 첫번째 경우
        if k == 0:
            d[i][k] = d[i-1][k] + A[i][k]
        elif i == k: # 마지막 경우
            d[i][k] = d[i-1][k-1] + A[i][k]
        else:
            d[i][k] = A[i][k] + max(d[i-1][k-1], d[i-1][k])


        
print(max(d[N-1]))