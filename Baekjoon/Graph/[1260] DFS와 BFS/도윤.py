from collections import deque

result = []
result2 = [] 

def dfs(graph, visited, i):
    visited[i] = True
    result.append(i)

    for k in graph[i]:
        if not visited[k]:
            dfs(graph, visited, k)

def bfs(graph, visited, i):
    queue = deque([i])
    visited[i] = True

    while queue:
        v = queue.popleft()
        result2.append(v)

        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True


# N = 노드, M = 간선, V = 시작점
N,M,V = map(int, input().split())

A = [[] for _ in range(N+1)]

visited = [False] * (N + 1)
visited2 = [False] * (N + 1)


for i in range(M):
    start,end = map(int, input().split())
    A[start].append(end) 
    A[end].append(start)

for k in A:
    k.sort()


dfs(A, visited, V)
bfs(A, visited2, V)


print(*result)
print(*result2)
