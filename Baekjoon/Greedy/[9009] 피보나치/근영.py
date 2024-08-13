N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

for i in range(N):
    temp = lst[i]

    # 1) 사용할 피보나치 수 리스트를 만듦
    curIdx = 2
    curVal = 1
    fibonacci = [0, 1]
    while curVal <= temp:
        next = fibonacci[curIdx - 2] + fibonacci[curIdx - 1]
        if next > temp : break
        fibonacci.append(next)
        curVal = next
        curIdx += 1

    # 2) temp가 0이 될 때까지 피보나치 리스트에서 큰 수부터 추가
    tempLst = []
    while temp > 0 :
        last = fibonacci.pop()
        if last <= temp : 
            tempLst.append(last)
            temp -= last
    
    tempLst.sort()
    print(*tempLst)