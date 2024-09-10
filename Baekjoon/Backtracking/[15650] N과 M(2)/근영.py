# [조건]
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = []
def backTracking(x):
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return
    for i in range(1, N+1):
        if i not in answer and i > x:
            answer.append(i)
            backTracking(i)
            answer.pop()

backTracking(0)