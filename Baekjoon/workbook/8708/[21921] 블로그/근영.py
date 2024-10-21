import sys
input = sys.stdin.readline

N, X = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = X
max_visit = 0
cnt = 1
for i in range(right):
    max_visit += lst[i]
temp = max_visit

while right < N :
    temp = temp - lst[left] + lst[right]

    if temp > max_visit:
        max_visit = temp
        cnt = 1
    elif temp == max_visit:
        cnt += 1

    left += 1
    right += 1

if max_visit :
    print(max_visit)
    print(cnt)
else :
    print("SAD")

# 슬라이딩 윈도우 - 유형 맞춤 ~~!