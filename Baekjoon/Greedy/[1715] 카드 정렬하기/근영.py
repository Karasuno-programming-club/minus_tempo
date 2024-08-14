import heapq

N = int(input())

# 1) 우선순위 큐 만들기
hq = []
for _ in range(1, N+1):
    heapq.heappush(hq, int(input()))

# 2) 앞의 두 개를 꺼내서 더한 뒤 다시 넣어 정렬(반복)
answer = 0
cnt = 0
while(cnt < N - 1):
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    next = first + second
    answer += next
    heapq.heappush(hq, next)
    cnt += 1

print(answer)