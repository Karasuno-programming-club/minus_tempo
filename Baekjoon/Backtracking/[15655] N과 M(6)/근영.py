# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
answer = []
def backTracking(x) :
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return

    for i in lst :
        if i not in answer and i > x:
            answer.append(i)
            backTracking(i)
            answer.pop()

backTracking(0)
