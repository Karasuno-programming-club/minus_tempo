from collections import deque

N, M, V = map(int, input().split())

# 1) 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
for i in range(M):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

# 2) 작은 노드부터 방문 -> sort
for i in range(N+1):
    lst[i].sort()


# 2) 방문한 노드 저장
visited = [0] * (N+1)

# 3) dfs
def dfs(start):
    visited[start] = 1
    print(start, end=" ")
    for i in lst[start]:
        if visited[i] == 0:
            dfs(i)

# 4) bfs
bfsVisited = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    bfsVisited[start] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in lst[v]:
            if not bfsVisited[i]:
                queue.append(i)
                bfsVisited[i] = 1

dfs(V)
print('')
bfs(V)