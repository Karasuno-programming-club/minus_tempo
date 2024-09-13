# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
def backTracking(x):
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return
    
    for i in lst:
        if i >= x :
            answer.append(i)
            backTracking(i)
            answer.pop()

backTracking(0)