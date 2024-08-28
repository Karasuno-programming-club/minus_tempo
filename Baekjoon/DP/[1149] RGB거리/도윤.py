d = [[0] * 3 for _ in range(100)]

N = int(input())

for i in range(N):
    RGB = list(map(int, input().split()))
    
    if i == 0:
        d[i][0] = RGB[0]
        d[i][1] = RGB[1]        
        d[i][2] = RGB[2]
    else:
        # d[i][0] = min(RGB[1], RGB[2]) + d[i-1][0]
        # d[i][1] = min(RGB[0], RGB[2]) + d[i-1][1]
        # d[i][2] = min(RGB[0], RGB[1]) + d[i-1][2]
        d[i][0] = min(d[i-1][1], d[i-1][2]) + RGB[0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + RGB[1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + RGB[2]

print(min(d[N-1]))


# ...