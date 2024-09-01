N = int(input())

# 사자가 없는 경우 , 윗칸에 사자가 있는경우, 아랫칸에만 사자가 있는 경우
prev = [1, 1, 1]

for i in range(2, N + 1):
    current = [
        (prev[0] + prev[1] + prev[2]) % 9901,
        (prev[0] + prev[2]) % 9901,
        (prev[0] + prev[1]) % 9901
    ]
    
    prev = current

result = sum(prev) % 9901
print(result)

# 사자 먹이로 들어가겠습니다.