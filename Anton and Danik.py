n = int(input())
y = input()
d = y.count("D")
a = y.count("A")
if d>a:
  print("Danik")
elif a>d:
  print("Anton")
else:
  print("Friendship")
