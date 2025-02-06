word = input()
k = []
for i in word:
  if not i in k:
    k.append(i)
l = len("".join(k))
if l %2 ==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
