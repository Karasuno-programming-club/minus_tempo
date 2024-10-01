import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = 0
graph = [[] for _ in range(M+1)]
for i in range(N):
    a, b, c = map(int, input().split())
    if a <= M :
        graph[a].append((b, c))
distance = [INF] * (M+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    end_point = 0

    while q:
        dist, now = heapq.heappop(q)
        end_point = now

        if distance[now] < dist :
            continue

        for i in graph[now]:
            # 도착점이 고속도로 길이보다 크면 지름길 이용하지 않음
            if i[0] > M :
                continue
            # 지름길을 사용하지 않는게 더 작을 경우 지름길을 이용하지 않음
            if i[0] - now <= i[1]:
                continue
                
            # 지름길 이용할 때
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

        # 도착점에 지름길이 없을 경우
        if end_point < M :
            heapq.heappush(q, [dist+1, now+1])
            if distance[now+1] > dist + 1 :
                distance[now+1] = dist + 1

dijkstra(0)
print(distance[-1])

# 이걸 풀다니 ~~~~~~~~~~~~ 미친 ~~~~~~~~