import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = 0

min_cost = cost[0]
for i in range(N-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    answer += min_cost * dist[i]

print(answer) 