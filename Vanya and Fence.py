n,h=map(int,input().split())
a = [int(i) for i in input().split()]
x = 0
for i in range(n):
  if a[i] > h:
    x += 2
  else:
    x +=1
print(x)
