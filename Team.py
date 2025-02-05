n = int(input())
u = []
k = 0
for i in range(n):
  x = [int(i) for i in input().split()]
  u.append(x)
for i in u:
  if sum(i) >= 2:
    k+=1
print(k)
