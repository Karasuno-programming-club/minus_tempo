import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    lst[end].append(start)

max_cnt = 0
answer = []

def bfs(start):
    queue = deque([start])
    cnt = 1

    while queue :
        v = queue.popleft()
        visited[v] = 1

        for i in lst[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

for i in range(1, N+1):
    visited = [0] * (N+1)
    cnt = bfs(i)

    if cnt > max_cnt:
        max_cnt = cnt
        answer = [i]
    elif cnt == max_cnt:
        answer.append(i)

print(*answer)
