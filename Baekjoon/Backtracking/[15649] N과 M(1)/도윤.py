def recursive(k):
    if(k == M+1):
        print(' '.join(map(str, selected[1:M+1])))
    else: 
        for i in range (1,N+1):
            if not used[i]:
                selected[k] = i
                used[i] = True
                recursive(k+1)
                selected[k] = 0
                used[i] = False

        



N,M = map(int,input().split())
selected = [0] * (M + 1)

used = [False] * (N + 1)

recursive(1)
