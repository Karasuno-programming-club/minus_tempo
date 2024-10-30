import sys
import heapq
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    cur = int(input())

    if cur == 0:
        if len(queue) == 0 :
            print(0)
        else :
            x = heapq.heappop(queue)
            print(x)
    else :
        heapq.heappush(queue, cur)