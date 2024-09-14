def dfs(n, lst):
    
    if n == M: 
        answer.append(lst)
        return 
    
    for j in sortedList:
        dfs(n+1, lst+[j])


N,M = map(int,input().split())
sortedList = sorted(list(map(int, input().split())))
answer = []

dfs(0, [])

for lst in answer:
    print(*lst)