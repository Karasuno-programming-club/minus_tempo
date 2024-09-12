def dfs(n, lst):
    
    # 종료 조건
    if n == M: 
        answer.append(lst)
        return 
    
    # 하부 함수 호출
    for j in range(1, N+1):
        dfs(n+1, lst+[j])

N,M = map(int,input().split())
answer =[]

dfs(0, [])

for lst in answer:
    print(*lst)