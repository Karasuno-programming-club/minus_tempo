import sys
sys.setrecursionlimit(10000)

def dfs(graph, x, y, color):
    
    if x < 0 or y < 0 or y >= len(graph) or x >= len(graph[0]) or graph[y][x] != color:
        return
       
    graph[y][x] = ''
    
    dfs(graph, x+1, y, color)
    dfs(graph, x-1, y, color)
    dfs(graph, x, y+1, color)
    dfs(graph, x, y-1, color)

N = int(input())

A = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for k in range(N):
    str = input()
    for i in range(len(str)):
        A[k].append(str[i])
        B[k].append("R" if str[i] == "G" else str[i])
        
resultA = 0        
resultB = 0
        
for y in range(N):
    for x in range(N):
        if A[y][x] != '':
            dfs(A, x, y, A[y][x])
            resultA += 1
        if B[y][x] != '':
            dfs(B, x, y, B[y][x])
            resultB += 1
            
print(*[resultA,resultB])
            
