# 재귀함수 쓸 때 필수
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

# bfs
def bfs():
    queue = deque([[startX, startY]])

    while queue:
        x, y = queue.popleft()
        if abs(x - festX) + abs(y - festY) <= 1000:
            print('happy')
            return
        for i in range(N):
            if not visited[i]:
                convX, convY = conv[i]
                if abs(x - convX) + abs(y - convY) <= 1000 :
                    visited[i] = 1
                    queue.append([convX, convY])
    print('sad')
    return

for _ in range(T):
    N = int(input()) # 편의점 수
    # 출발점
    startX, startY = map(int, input().split())
    # 편의점
    conv = []
    for _ in range(N):
        conv.append(list(map(int, input().split())))
    # 락페
    festX, festY = map(int, input().split())

    # 방문 기록
    visited = [0 for _ in range(N+1)]
    bfs()    