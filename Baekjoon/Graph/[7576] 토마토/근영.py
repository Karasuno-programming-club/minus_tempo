from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
queue = deque([])
cnt = 0
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 이차원 배열  
field = [list(map(int, input().split())) for _ in range(N)]

# 익은 토마토(1)가 있는 위치를 찾아서 큐에 넣는다
for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            queue.append([j, i, 1])

# bfs
def bfs():
    while queue:
        x, y, dis = queue.popleft()

        for m in move :
            X, Y = m[0] + x, m[1] + y

            if(0 <= X < M and 0 <= Y < N) and (field[Y][X] == 0 or field[Y][X] > dis+1):
                field[Y][X] = dis+1
                queue.append([X, Y, dis+1])

bfs()

# 0이 있으면 모두 익지 못하는 상태 -> -1 출력
for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            print(-1)
            exit(0)
        else :
            cnt = max(cnt, field[i][j])
            
print(cnt-1)