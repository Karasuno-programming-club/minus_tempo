def dfs(n, cur, lst):
    
    if n == M: 
        answer.append(lst)
        return 
    
    for j in sortedList:
        if j >= cur:
            dfs(n+1, j, lst+[j])


N,M = map(int,input().split())
sortedList = sorted(list(map(int, input().split())))
answer = []

dfs(0, 0, [])

for lst in answer:
    print(*lst)