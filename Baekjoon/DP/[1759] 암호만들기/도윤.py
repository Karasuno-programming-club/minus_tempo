def dfs(n, start, result):

    if n == N and Acount[0] >= 1 and (n - Acount[0]) >= 2: 
        ans.append(result)
        return
    
    for i in range(start, M):
        if A[i] in vowel:
            Acount[0] = Acount[0] + 1
        dfs(n+1, i+1, result + [A[i]])
        if A[i] in vowel:
            Acount[0] = Acount[0] - 1

N, M = map(int, input().split())
A = sorted(list(input().split()))

vowel = ["a", "e", "i", "o", "u"]
Acount = [0]
ans = []

dfs(0, 0, [])

for k in ans:
    print(''.join(k))
