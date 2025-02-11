a1, a2, a3, a4 = map(int, input().split())
s = input().strip()

c = { '1': a1, '2': a2, '3': a3, '4': a4 }

t = sum(c[ch] for ch in s)

print(t)
