import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

value = roll()
print(value)

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else: 
            print("Must be between 2 - 4 players.")

    else: 
        print("Invalid, try again.")
        
max_score = 50      
print(players)