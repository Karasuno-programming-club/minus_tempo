from collections import deque

def bfs(field, x, y, queue):
    maxDay = 0

    while queue: 

        v = queue.popleft()
        x = v[0]
        y = v[1]
        count = v[2]

        if(maxDay < count):
            maxDay = count
        
        if x > 0 and field[y][x-1] == 0:
            queue.append((x-1, y, count + 1))
            field[y][x-1] = 2
        
        if x < (len(field[0]) - 1) and field[y][x+1] == 0:
            queue.append((x+1, y, count + 1))
            field[y][x+1] = 2

        if y > 0 and field[y-1][x] == 0:
            queue.append((x, y-1, count + 1))
            field[y-1][x] = 2

        if y < (len(field) -1) and field[y+1][x] == 0:
            queue.append((x, y+1, count + 1))
            field[y+1][x] = 2

    return maxDay


row, col = map(int, input().split())

A = []

for _ in range(col):
    A.append(list(map(int, input().split())))


queue = deque()

for y in range(col):
    for x in range(row):
        if A[y][x] == 1:
            queue.append((x,y,0))

result = bfs(A, x, y, queue)

isFail = False

for y in range(col):
    for x in range(row):
        if A[y][x] == 0:
            isFail = True
            break

print(-1 if isFail else result)

