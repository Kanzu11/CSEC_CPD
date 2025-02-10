n = int(input())
cards = list(map(int, input().split()))

sereja = 0
dima = 0
left = 0
right = n - 1
turn = 0

while left <= right:
    if cards[left] > cards[right]:  
        card = cards[left]
        left += 1
    else:
        card = cards[right]
        right -= 1
    
    if turn % 2 == 0: 
        sereja += card
    else:  
        dima += card
    
    turn += 1 

print(sereja, dima)
