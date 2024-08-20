import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

# 이차원 배열 만들기
field = []
for i in range(N):
    field.append(list(input().strip("\n")))

move = [[1,0], [0, -1], [-1, 0], [0, 1]]

# bfs
def bfs(startX, startY, cur):
    queue = deque([[startX, startY]])

    while queue:
        x, y = queue.popleft()

        visited[y][x] = 1

        for m in move: 
            X = m[0] + x
            Y = m[1] + y

            if (0 <= X < N and 0 <= Y < N) and visited[Y][X] == 0 and field[Y][X] in cur:
                queue.append([X, Y])
                visited[Y][X] = 1

# 정상, 적록색약
cases = [[["R"], ["G"], ["B"]], [["R", "G"], ["B"]]]

for case in cases:
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for c in case:
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and field[i][j] in c:
                    bfs(j, i, c)
                    cnt += 1
    print(cnt)
        