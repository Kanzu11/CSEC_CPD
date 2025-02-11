s = input().strip()  
t = 0
pos = 'a'  

for char in s:
    clockwise = abs(ord(char) - ord(pos))
    counterclockwise = 26 - clockwise
    t += min(clockwise, counterclockwise)
    
    pos = char

print(t)
