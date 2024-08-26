A = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
d = A + [[1] * 14 for _ in range(14)]

def cal(floor, room): 
    
    for j in range(1, floor+1):
        for i in range(1, room):
            d[j][i] = d[j][i-1] + d[j-1][i]
    
    return d[floor][room-1]
    


N = int(input())

for _ in range(N):
    # K층
    K = int(input())
    # 호
    N = int(input())
    
    print(cal(K,N))
    
    
# 하 머리 깨질뻔했네