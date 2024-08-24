import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y, count):
    global max_count

    max_count = max(max_count, count)
    
    if max_count == 26:  # 알파벳의 개수는 26개가 최대
        return
    
    for moveX, moveY in [(0,1), (1,0), (-1,0), (0,-1)]:
        nx = x + moveX
        ny = y + moveY
        if 0 <= nx < len(A[0]) and 0 <= ny < len(A) and A[ny][nx] not in visited:
            visited.add(A[ny][nx])  # 다음 칸 방문
            dfs(nx, ny, count + 1)
            visited.remove(A[ny][nx])  # 백트래킹

R, C = map(int, input().split())
A = [list(input().strip()) for _ in range(R)]

visited = set([A[0][0]])
max_count = 1

dfs(0, 0, 1)
print(max_count)


# 백트래킹으로 풀어야함
# 파이썬으로 속도가 느려서 pypy로 제출해야함