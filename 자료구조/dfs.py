# https://www.acmicpc.net/problem/2606 이용
# [입력] 
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

N = int(input()) # N개의 노드(1~N)
M = int(input()) # M개의 간선

# 1) 인접 리스트 만들기
lst = [[] for _ in range(N+1)]
for i in range(2, N+1):
    start, end = map(int, input().split())
    lst[start].append(end)
    lst[end].append(start)

# 2) 방문했던 노드 저장할 리스트
visited = [False] * (N + 1)

# 3) dfs
def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(lst, 1, visited)
