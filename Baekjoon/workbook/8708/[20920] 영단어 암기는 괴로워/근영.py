N, M = map(int, input().split())
count = {}

for _ in range(N):
    word = input()

    if len(word) < M :
        continue
    
    if word in count :
        count[word] += 1
    else :
        count[word] = 1

lst = sorted(count.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i in lst:
    print(i[0])