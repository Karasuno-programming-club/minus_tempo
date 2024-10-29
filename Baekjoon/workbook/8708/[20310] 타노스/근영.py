S = list(input())
init_1 = S.count("1")
init_0 = len(S) - init_1

# 1은 앞에서부터 없앤다
cnt = 0
while cnt < init_1 // 2:
    for i in range(len(S)):
        if S[i] == "1":
            S[i] = ""
            cnt += 1
            break

# 0은 뒤에서부터 없앤다
cnt = 0
while cnt < init_0 // 2:
    for i in reversed(range(len(S))):
        if S[i] == "0":
            S[i] = ""
            cnt += 1
            break

print("".join(S))