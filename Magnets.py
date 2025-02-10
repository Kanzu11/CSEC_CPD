n = int(input())
m = [input().strip() for _ in range(n)]

t = 1

for i in range(1, n):
    if m[i] != m[i - 1]:
        t += 1

print(t)
