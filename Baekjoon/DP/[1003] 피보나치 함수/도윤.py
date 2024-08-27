d = [[0] * 2 for _ in range(3000)]

d[0][0] = 1
d[1][1] = 1 

def fibonacci(n):
    
    for i in range(2, n+1):
        d[i][0] = d[i-2][0] + d[i-1][0]
        d[i][1] = d[i-2][1] + d[i-1][1]
        
    print(*d[n], sep=" ")
    
N = int(input())

for _ in range(N):
    A = int(input())
    fibonacci(A)