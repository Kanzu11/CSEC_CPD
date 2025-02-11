n = int(input())
b = list(map(int, input().split()))
m = int(input())
for _ in range(m):
  x, y = map(int, input().split())
  x -= 1
  y -= 1 
  if x > 0:
    b[x - 1] += y 
  if x < n - 1:
    b[x + 1] += (b[x] - (y + 1))
    b[x] = 0
for i in b:
  print(i)
