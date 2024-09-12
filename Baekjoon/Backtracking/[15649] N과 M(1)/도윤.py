def dfs(n, lst):
    
    # 종료 조건
    if n == M: 
        answer.append(lst)
        return 
    
    # 하부 함수 호출
    for j in range(1, N+1):
        if v[j] == 0: #선택되지 않은 경우 추가
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

N,M = map(int,input().split())
answer =[]
v = [0] * (N + 1)

dfs(0, [])

for lst in answer:
    print(*lst)
    
    
    
# 재학습1