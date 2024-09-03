# 동전문제

# K 결과
N, K = map(int, input().split())

A = []

for i in range(N):
    A.append(int(input()))


d = [0] * (K+1)
d[0] = 1

for i in A:
    for j in range(i, K+1):
        d[j] += d[j - i]
        
print(d[K])
