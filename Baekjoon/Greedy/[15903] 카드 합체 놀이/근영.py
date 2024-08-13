import heapq

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 1) 최소 힙 만들기
heapq.heapify(lst)

# 2) 카드 합체
for i in range(M):
    least1 = heapq.heappop(lst)
    least2 = heapq.heappop(lst)
    total = least1 + least2
    heapq.heappush(lst, total)
    heapq.heappush(lst, total)

print(sum(lst))