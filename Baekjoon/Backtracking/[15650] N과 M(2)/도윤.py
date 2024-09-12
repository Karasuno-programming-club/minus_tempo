def dfs(n, lst):
    if n > N: 
        if len(lst) == M:
            ans.append(lst)
        return

    dfs(n+1, lst+[n]) # 선택하는 경우
    dfs(n+1, lst) # 선택하지 않는 경우



N,M = map(int, input().split())
ans = []
dfs(1, [])

for lst in ans:
    print(*lst)


## 다른 풀이2
def dfs(n, start, lst):
    
    # 종료 조건
    if n == M: 
        answer.append(lst)
        return 
    
    # 하부 함수 호출
    for j in range(start, N+1):
        dfs(n+1, j+1, lst+[j])

N,M = map(int,input().split())
answer =[]
v = [0] * (N + 1)

dfs(0, 1, [])

for lst in answer:
    print(*lst)


## 다시 공부 중