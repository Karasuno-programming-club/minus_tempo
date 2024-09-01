N = int(input())

if N == 1:
    print(int(input()))
    exit(0)
    
A = []

for _ in range(N):
    A.append(int(input()))

if N == 2:
    print(A[0] + A[1])
    exit(0)


d = [0] * N
 

d[0] = A[0]
d[1] = A[0] + A[1]
d[2] = max(A[0] + A[2], A[1] + A[2], d[1])

for i in range(3, N):
    d[i] = max(d[i-1], d[i-2] + A[i], d[i-3] + A[i-1] + A[i])


print(d[-1])