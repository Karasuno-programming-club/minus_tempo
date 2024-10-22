N, K = map(int, input().split())
table = list(input())

cur_ham = 0
cur_man = 0
cnt = 0

while cur_ham < N and cur_man < N :
    if table[cur_ham] != "H":
        cur_ham += 1
    elif table[cur_man] != "P":
        cur_man += 1
    else:
        if(abs(cur_ham - cur_man)) <= K:
            cnt += 1
            cur_ham += 1
            cur_man += 1
        else :
            if cur_ham > cur_man:
                cur_man += 1
            else :
                cur_ham += 1

print(cnt)
