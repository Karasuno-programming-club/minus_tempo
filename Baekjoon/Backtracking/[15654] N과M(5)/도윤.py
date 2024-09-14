def dfs(n, lst):
    
    if n == M: 
        answer.append(lst)
        return 
    

    for j in sortedList:
        if j not in lst : #선택되지 않은 경우 추가
            dfs(n+1, lst+[j])

N,M = map(int,input().split())

sortedList = sorted(list(map(int, input().split())))

answer =[]
v = [0] * (N + 1)

dfs(0, [])

for lst in answer:
    print(*lst)
    
# KT 화이팅 DEFT 화이팅