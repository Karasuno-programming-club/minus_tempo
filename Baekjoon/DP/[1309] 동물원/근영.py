N = int(input())

# 한 줄에 가능한 경우의 수 : XX, XO, OX
# 1) 바로 윗 줄이 XX일 경우 : 모든 경우의 수
# 2) 바로 윗 줄이 XO일 경우 : OX, XX 경우
# 3) 바로 윗 줄이 OX일 경우 : XO, XX 경우

a = 1
b = 1
c = 1

for i in range(2, N+1): 
    a, b, c = a+b+c, a+c, a+b

print((a+b+c) % 9901)