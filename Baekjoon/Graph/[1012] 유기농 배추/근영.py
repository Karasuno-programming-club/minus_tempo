import sys
sys.setrecursionlimit(10000)

T = int(input())
# dfs 정의
def dfs(y, x):
    if field[y][x] == 1 :
        field[y][x] = 0 # 방문 기록
        # 상하 확인
        for _y in [1, -1]:
            Y = _y + y
            if(Y >= 0 and Y < h) and field[Y][x] == 1 :
                dfs(Y, x)
            
         # 좌우 확인
        for _x in [1, -1]:
            X = _x + x
            if(X >= 0 and X < w) and field[y][X] == 1 :
                dfs(y, X)

for _ in range(T):
    w, h, cab = map(int, input().split())

    # 필드 0으로 초기화
    field = [[0 for _ in range(w)] for _ in range(h)]
    
    # 위치 좌표 표시
    for i in range(cab):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    
    
    # 카운트
    cnt = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1 :
                dfs(i, j)
                cnt+= 1
    
    print(cnt)