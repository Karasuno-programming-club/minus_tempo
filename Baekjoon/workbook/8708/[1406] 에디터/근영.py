import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

M = int(input())
for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == "L" and len(left) > 0 :
        right.append(left.pop())
    elif cmd[0] == "D" and len(right) > 0 :
        left.append(right.pop())
    elif cmd[0] == "B" and len(left) > 0 :
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[1])

answer = left + right[::-1]
print(''.join(answer))