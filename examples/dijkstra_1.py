# 1) 순차탐색
# 시간복잡도 : O(N²)
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 = 10억으로 설정

# N : 노드의 개수, M : 간선의 개수
N, M = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(N+1)]
# 방문 체크
visited = [0] * (N+1)
# 최단 거리 테이블 - 무한으로 초기화
distance = [INF] * (N+1)

# 모든 간선 정보를 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c이다
    graph[a].append([b, c])

# 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 거리가 짧은 노드(인덱스)
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 N-1개의 노드에 대해 반복
    for i in range(N-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = 1
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, N+1):
    if distance[i] == INF:
        print('도달할 수 없음')
    else :
        print(distance[i])