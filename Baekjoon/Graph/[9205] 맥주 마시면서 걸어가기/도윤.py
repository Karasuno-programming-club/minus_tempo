from collections import deque

T = int(input())

answer = []

for _ in range(T):
    
    # 편의점 개수
    A = int(input()) 
    
    inputs = []
    
    # 시작
    startX, startY = map(int, input().split())
    queue = deque()
    queue.append((startX, startY))    
    result = "sad"

    
    # 편의점 + 끝
    for i in range(A):
        x,y = map(int, input().split())
        inputs.append((x,y))
        
    endX, endY = map(int, input().split())
    inputs.append((endX, endY))
    
    visited = set()


    while queue:

        x,y = queue.popleft()
        
        if abs(endX -x) + abs(endY- y) <= 1000:
            result = "happy"
            break
        
        for nx, ny in inputs:
            if (nx, ny) not in visited and abs(nx - x) + abs(ny - y) <= 1000:
                queue.append((nx, ny))
                visited.add((nx, ny))
        
    answer.append(result)
    
print(*answer, sep='\n')