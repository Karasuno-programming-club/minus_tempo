N = int(input())

# 1) 자릿수 스코어 저장하는 딕셔너리 만들기
posDic = {}
for n in range(N):
    temp = input()
    length = len(temp)
    for i in range(length):
        pos = 10 ** (length - i - 1)
        if temp[i] in posDic : posDic[temp[i]] += pos
        else : posDic[temp[i]] = pos
        
# 2) 스코어 순으로 sort
sortedDic = dict(sorted(posDic.items(), key=lambda item:item[1], reverse=True))

# 3) 숫자 분배
dic = {}
num = 9
for letter, pos in sortedDic.items():
    dic[letter] = num
    num-= 1

# 4) 꺼내서 더한다
answer = 0
for letter, pos in sortedDic.items():
    answer += pos * dic[letter]

print(answer)