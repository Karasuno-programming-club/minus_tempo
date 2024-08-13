import math

N = int(input())
lst = []

for i in range(N):
    temp = []
    temp.append(int(input()))
    temp.append(list(map(int, input().split())))
    lst.append(temp)

for i in range(N):
    T, cases = lst[i]
    
    # 1) 오름차순으로 sort
    cases.sort()

    # 2) 중간값 기준 홀수는 앞에, 짝수는 뒤에 배치해 리스트를 만든다
    temp = [0 for k in range(T)]
    middle = T // 2 # 중간값에서 시작한다

    for j in range(T):
        idx = middle
        if j % 2 == 0 :
           idx += j // 2
        else :
           idx -= math.ceil(j / 2)
        
        temp[idx] = cases[j]
    
    # 3) 절댓값의 최댓값을 구한다
    max = 0
    for j in range(T):
        gap = abs(temp[j] - temp[j-1])
        if(max < gap):
            max = gap

    print(max)