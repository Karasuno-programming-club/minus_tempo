import sys
input = sys.stdin.readline

R,C = map(int, input().split())

board = []
for i in range(R):
    board.append(list(input().strip()))

alp = set(board[0][0])

moves = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# dfs
answer = 0
def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    for m in moves :
        X = m[0] + x
        Y = m[1] + y

        if X < 0 or Y < 0 or X >= C or Y >= R: continue

        elif board[Y][X] not in alp:
            alp.add(board[Y][X])
            dfs(X, Y, cnt+1)
            alp.remove(board[Y][X]) # 백트래킹

dfs(0,0,1)
print(answer)