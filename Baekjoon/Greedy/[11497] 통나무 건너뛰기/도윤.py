T = int(input())

result = []

for i in range(T):
    N = int(input())
    M = list(map(int, input().split()))
    
    M.sort()
    
    arr = [0 for i in range(N)]
    start = 0
    end = len(M) - 1

    for index in range(N):
        if(index % 2 == 0):
            arr[start] = M[index] 
            start += 1
        else:
            arr[end] = M[index] 
            end -= 1
    

    max = abs(arr[-1] - arr[0])

    for idx in range(N-1):
        interval = abs(arr[idx] - arr[idx+1])
        if (interval > max):
            max = interval

    result.append(max) 
    

for k in result:
    print(k)

