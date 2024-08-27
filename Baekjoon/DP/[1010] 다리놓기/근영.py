import sys
input = sys.stdin.readline
import math

T = int(input())

for _ in range(T):
    left, right = map(int, input().split())
    
    res = math.comb(right, left)
    print(res)
