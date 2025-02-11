import math

Y, W = map(int, input().split())
m = max(Y, W)
f = 6 - m + 1
gcd = math.gcd(f, 6)

print(f"{f // gcd}/{6 // gcd}")
