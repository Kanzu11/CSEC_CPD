s = input().strip()
upper_count = 0

for char in s:
    if char.isupper():
        upper_count += 1
if upper_count > len(s) // 2:
    print(s.upper())
else:
    print(s.lower())
