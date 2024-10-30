import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cur_keywords = {}

for _ in range(N):
    keyword = input().strip()
    cur_keywords[keyword] = 0

cnt = 0
for _ in range(M):
    lst = list(map(lambda x:x.strip(), input().split(",")))
    
    for i in lst :
        try:
            if cur_keywords[i]:
                continue
            else:
                cur_keywords[i] += 1
                cnt += 1
        except:
            continue

    print(N - cnt)
