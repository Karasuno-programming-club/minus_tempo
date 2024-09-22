def cal(lst):
    total = 0
    for i,j in home: #집 좌표 
        mn = 2 * N
        for ci,cj in lst:
            mn = min(mn, abs(i-ci)+abs(j-cj))
        total += mn
    return total    
    

def dfs(n, lst):
    global ans
    if n == CNT: 
        if len(lst) == M: # M개 유지 결정시 최소값
            ans = min(ans, cal(lst))
        return
    
    # 유지 케이스
    dfs(n+1, lst+[chicken[n]])
    # 폐업 케이스
    dfs(n+1, lst)
    
    
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))
                        
CNT = len(chicken)

ans = 2*N*2*N
dfs(0,[])

print(ans)

# 저한테 겁.나.어.렵.습.니.다.