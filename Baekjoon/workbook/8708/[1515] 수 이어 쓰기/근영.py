import sys
input = sys.stdin.readline

num = input().strip()
n = 0

while len(num):
    n += 1
    temp = str(n)
    while len(temp) and len(num):
        if temp[0] == num[0]:
            num = num[1:]
        temp = temp[1:]
print(n)