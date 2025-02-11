k, r = map(int, input().split())

n = 1  
while True:
    t = n * k
    if t % 10 == 0 or t % 10 == r:
        print(n)
        break
    n += 1
