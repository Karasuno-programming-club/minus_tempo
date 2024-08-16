import sys
sys.setrecursionlimit(10000)

def dfs(field, x, y):
    if x < 0 or y < 0 or x >= len(field) or y >= len(field[0]) or field[x][y] == 0:
        return

    field[x][y] = 0  # 방문 처리

    # 상하좌우 탐색
    dfs(field, x, y+1)
    dfs(field, x+1, y)
    dfs(field, x, y-1)
    dfs(field, x-1, y)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    result = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:  # 아직 방문하지 않은 배추일 때만
                dfs(field, y, x)
                result += 1

    print(result)