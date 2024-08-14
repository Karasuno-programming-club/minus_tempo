from queue import PriorityQueue

N = int(input())
M = [int(input()) for _ in range(N)]



que = PriorityQueue(maxsize=N)

result = 0

if(N <= 1):
    result =0
else:
    for k in M:
        que.put(k)

    while(que.qsize() > 1):
        sum = que.get() + que.get()
        result += sum
        que.put(sum)

print(result)