import sys
input = sys.stdin.readline

# 입력 받기 + 기둥 최댓값 구하기
N = int(input())
high = [0, 0]
lst = []
for i in range(N):
    idx, height = list(map(int, input().split()))
    lst.append([idx, height])

# index 순으로 정렬
lst.sort(key=lambda x:x[0])

# 최댓값 구하기
for i in range(N):
    if lst[i][1] > high[1]:
        high = [i, lst[i][1]]

# 최대 높이 전까지 합하기
answer = 0
max = lst[0]
for i in range(1, high[0]+1):
    if lst[i][1] >= max[1] :
        answer += (lst[i][0] - max[0]) * max[1]
        max = lst[i]

# 거꾸로 최대 높이까지 합하기
max = lst[N-1]
for i in range(N-2, high[0]-1, -1):
    if lst[i][1] >= max[1]:
        answer += (max[0]- lst[i][0]) * max[1]
        max = lst[i]

# 최대 기둥 높이 합하기
answer += high[1]

print(answer)