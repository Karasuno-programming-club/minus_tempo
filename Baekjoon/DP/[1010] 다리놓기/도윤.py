d = [0] * 30

def factorial(x): 
  if x == 0: return 1
        
  d[1] = 1
  
  for i in range(2, x+1):
    d[i] = d[i-1] * i
      
  return d[x]

    

N = int(input())
answer = [] 
for _ in range(N):
  A, B = map(int, input().split())
  result = int(factorial(B) / (factorial(A) * factorial(B-A)))
  answer.append(result)

print(*answer, sep="\n")