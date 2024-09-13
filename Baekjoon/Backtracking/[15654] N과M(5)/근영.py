N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
def backTracking():
    if len(answer) == M : 
        print(" ".join(map(str, answer)))
        return
    
    for i in lst :
        if i not in answer :
            answer.append(i)
            backTracking()
            answer.pop()

backTracking()