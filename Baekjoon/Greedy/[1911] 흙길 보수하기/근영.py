import math

N, M = map(int, input().split())
lst = [(list(map(int, input().split()))) for _ in range(N)]

# 1) 오름차순 정렬
lst.sort(key=lambda x:x[0])

# 2) 다리 끝 지점 저장하며 카운트
count = 0
last = 0

for i in range(N):
    start, end = lst[i]
    if last <= start :
        last = start
    
    temp = math.ceil((end - last) / M)
    count += temp
    last += M * temp

print(count)

