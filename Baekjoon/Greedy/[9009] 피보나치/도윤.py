def make(arr, limit):
  a = arr[0]
  b = arr[1]

  while(a + b <= limit): 
    sum = a + b
    arr.append(sum)
    a = b 
    b = sum

  return arr    


N = int(input())
M = [int(input()) for _ in range(N)]

for k in M: 
  pibonacci = make([1,1], k)
  result = []

  for i in reversed(pibonacci):
    if (i <= k):
      result.append(i)
      k = k - i

  result.reverse()         
  print(*result)