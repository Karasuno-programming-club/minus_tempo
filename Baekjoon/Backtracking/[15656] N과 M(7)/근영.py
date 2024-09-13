# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
def backTracking():
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return

    for i in lst:
        answer.append(i)
        backTracking()
        answer.pop()

backTracking()