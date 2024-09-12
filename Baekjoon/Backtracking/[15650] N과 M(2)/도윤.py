def recursive(k):
    if k == M:
        print(' '.join(map(str, selected[0:M])))
    else: 
        for i in range (1,N+1):
            if not used[i] and (k == 0 or i > selected[k-1]): 
                selected[k] = i
                used[i] = True
                recursive(k+1)
                selected[k] = 0
                used[i] = False

        



N,M = map(int,input().split())
selected = [0] * (M + 1)
used = [False] * (N + 1)
recursive(0)

