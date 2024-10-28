# 이 문제가 DP였다니,,
# 개어려움 ㅋㅌㅋ

import sys
input = sys.stdin.readline
H, W = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(H)]

INF = 601
record = [[[0]*3 for i in range(W+1)] for _ in range(2)]
for i in range(3):
    record[0][W][i] = INF
    record[1][W][i] = INF

p = 0

for h in range(H):
    np = (p+1) % 2
    for w in range(W):
        record[np][w][0] = cost[h][w] + min(record[p][w-1][1],record[p][w-1][2])
        record[np][w][1] = cost[h][w] + min(record[p][w][0], record[p][w][2])
        record[np][w][2] = cost[h][w] + min(record[p][w+1][0], record[p][w+1][1])
    p = np

value = INF
for c in range(W):
    value = min(value,min(record[p][c]))

print(value)