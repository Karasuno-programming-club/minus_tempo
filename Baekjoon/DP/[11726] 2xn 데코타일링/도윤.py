d = [0] * 1001

d[1] = 1
d[2] = 2


N = int(input())

for i in range(3, N+1):
    d[i] = d[i-2] + d[i-1]
    
    
print(d[N] % 10007)
