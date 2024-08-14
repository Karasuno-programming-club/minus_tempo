N = int(input())
M = [input() for _ in range(N)]
dic = {}

numbers = ['9','8','7','6','5','4','3','2','1','0']
np = 0

M.sort(key=len, reverse=True)

# 역순으로 문자열 묶어버림
for word in M:
    idx = len(word) - 1
    for i in range(len(word)):
        if(word[i] not in dic): 
            dic[word[i]] = 10 ** (idx - i)
        else: 
            dic[word[i]] += 10 ** (idx - i)


result = dic.values()
sum = 0

for k in sorted(result, reverse=True):
    sum += k * int(numbers[0])
    numbers = numbers[1:]
 

print(sum)