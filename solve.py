# 6 4
# 5 8 5 1
# 3 5 8 4
# 9 77 65 5
# 2 1 5 2
# 5 98 1 5
# 4 95 67 58
import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
moves = [[0, 1], [1, 1], [-1, 1]]
space = []
for _ in range(H):
    space.append(list(map(int, input().split())))

visited = [[0 for _ in range(W)] for _ in range(H)]

def bfs(startX, startY):
    queue = deque([[startX, startY]])
    cost = space[startY][startX]

    while queue:
        x, y = queue.popleft()

        for m in moves :
            X = m[0] + x
            Y = m[1] + y

            if X < 0 or X >= W or Y < 0 or Y >= H or visited[Y][H]:
                continue
            
            queue.append([X, Y])
            visited[Y][X] = 1
            cost += space[Y][X]
    return cost

for i in range(W):