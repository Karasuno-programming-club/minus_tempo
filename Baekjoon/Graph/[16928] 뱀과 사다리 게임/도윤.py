from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 사다리 수 , 뱀의 수 
N, M = map(int, input().split())

A = [1] * 101


# 사다리
ladder = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
    
# 뱀
snake = {}
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b


queue = deque([(1, 0)])

while queue:
    v, count = queue.popleft()
    
    if v == 100:
        print(count)
        break
    
    for k in range(1, 7):
        next = v + k
        
        if next <= 100:  
            if next in ladder:
                next = ladder[next]
            elif next in snake:
                next = snake[next]
                
        if next <= 100 and A[next] != -1:
            A[next] = -1
            queue.append((next, count+1))
            
# 어려움