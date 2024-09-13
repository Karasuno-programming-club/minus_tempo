# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

def dfs(n, s, lst):
    if n == M: 
        ans.append(lst)
        return

    
    for j in range(s, N+1):
        dfs(n+1, j, lst+[j])

N,M = map(int, input().split())
ans = []
dfs(0, 1, [])

for lst in ans:
    print(*lst)