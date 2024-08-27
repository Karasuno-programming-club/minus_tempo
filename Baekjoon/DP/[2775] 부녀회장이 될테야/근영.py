T = int(input())

for _ in range(T):
    floor = int(input())
    num = int(input())

    apart = [i for i in range(1, num+1)]

    for i in range(floor):
        for j in range(1, num):
            apart[j] += apart[j-1]
    

    print(apart[-1])