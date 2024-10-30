import sys
input = sys.stdin.readline

N, M = map(int, input().split())
names = []
values = []
for _ in range(N):
    name, value = input().split()
    names.append(name)
    values.append(int(value))


for _ in range(M):
    cur = int(input())
    start = 0
    end = N - 1


    while start < end :
        mid = (start + end) // 2

        if cur <= values[mid] :
            end = mid
        else :
            start = mid + 1
    print(names[start])