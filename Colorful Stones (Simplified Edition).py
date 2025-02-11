s = input()
t = input()

pos = 0

for c in t:
    if pos < len(s) and s[pos] == c:
        pos += 1

print(pos + 1)
