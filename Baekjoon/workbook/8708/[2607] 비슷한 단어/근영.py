T = int(input())
first = input()
answer = 0

for _ in range(T-1):
    compare = list(first)
    word = input()
    cnt = 0 # first 단어에 포함되지 않은 word의 문자의 개수
    # compare에 남아있는 문자들은 word에 포함되지 않은 문자들

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)