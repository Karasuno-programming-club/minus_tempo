# [조건]
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

N, M = map(int, input().split())

answer = []
def backTracking():
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        answer.append(i)
        backTracking()
        answer.pop()

backTracking()