import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 입력 받기, 인접 리스트
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, [cost, i])
dijkstra(X)

answer = []
for i in range(1, N+1):
    if distance[i] == K:
        answer.append(i)

answer.sort()

if len(answer):
    for n in answer:
        print(n)
else :
    print(-1)