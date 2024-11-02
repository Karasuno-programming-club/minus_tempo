import sys
input = sys.stdin.readline

P, M = list(map(int, input().split()))
rooms = []

for _ in range(P):
    level, name = list(input().rstrip().split())
    level = int(level)
    flag = False

    for room in rooms:
        key = room[0][0]
        if key - 10 <= level <= key + 10:
            if len(room) < M :
                room.append((level, name))
                flag = True
                break
    if not flag :
        rooms.append([(level, name)])

for room in rooms:
    if len(room) == M :
        print("Started!")
    else :
        print("Waiting!")
    
    for player in sorted(room, key=lambda x:x[1]):
        print(*player)