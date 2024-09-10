import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

# def 재귀함수(x):
#     if 정답이라면 :
#         정답 출력
#     else :
#         for 모든 자식 노드에 대해 :
#             if 정답에 유망하다면 :
#                 자식 노드로 이동
#                 재귀함수(x+1)
#                 부모 노드로 이동

def backtracking():
    if len(answer) == M :
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()