import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
T = int(input())
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(T):
    # 입력 받기
    H, W = map(int, input().split())
    field = [['.' for j in range(W)] for i in range(H)]

    for i in range(H):
        field[i] = list(input().strip())

    # bfs
    def bfs(startX, startY):
        queue = deque([[startX, startY]])
        
        while queue:
            y, x = queue.popleft()
            field[y][x] = '.'

            for m in moves :
                X = x + m[0]
                Y = y + m[1]

                if X < 0 or X >= W or Y < 0 or Y >= H or field[Y][X] == '.': continue
                field[Y][X] = '.'
                queue.append([Y, X])

    # 양일때만 bfs를 실행한다
    cnt = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] == '#':
                bfs(i, j)
                cnt += 1
    
    print(cnt)
