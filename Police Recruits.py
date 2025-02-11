n = int(input())
events = list(map(int, input().split()))
o = 0
u = 0 
for event in events:
  if event > 0:
    o += event
  elif event == -1:
    if o > 0:
      o -= 1 
    else: 
      u += 1
print(u)
