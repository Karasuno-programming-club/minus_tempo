# [조건]
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.

N, M = map(int, input().split())

answer = []
def backTracking(x):
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return
    else :
        for i in range(1, N+1):
            if i >= x :
                answer.append(i)
                backTracking(i)
                answer.pop()

backTracking(0)