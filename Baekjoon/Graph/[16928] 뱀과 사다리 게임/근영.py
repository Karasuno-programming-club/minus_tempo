import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

# 1) 뱀, 사다리를 저장한다
ladders = {} # 사다리
snakes = {} # 뱀(출발점만 저장)
for i in range(N):
    start, end = map(int, input().split())
    ladders[start] = end 
for i in range(M):
    start, end = map(int, input().split())
    snakes[start] = end

moves = [6, 5, 4, 3, 2, 1]
visited = [0] * 101

# bfs
queue = deque([[1, 0]])
visited[1] = 0

while queue:
    v, cnt = queue.popleft()

    if v == 100 :
        print(cnt)
        break
    else :
        for m in moves:
            next = v + m
            
            if next <= 100 and (visited[next] == 0 or visited[next] > cnt+1):
                visited[next] = cnt+1

                # 사다리칸
                if next in ladders.keys():
                    visited[ladders[next]] = cnt+1
                    queue.append([ladders[next], cnt+1])
                # 뱀칸
                elif next in snakes.keys():
                    visited[snakes[next]] = cnt+1
                    queue.append([snakes[next], cnt+1])
                # 아무것도 아닌 칸
                else :
                    queue.append([next, cnt+1])
            
