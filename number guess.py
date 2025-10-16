import random
total_points = 0
guess= int(input("Enter your guess:"))
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total_dice = dice1 + dice2
points = 0
if guess == total_dice:
       points = 10
elif abs(total_dice - guess) <= 2:
       points = 5
elif abs(total_dice - guess) <= 4:
       points = 1
else:
       points =  0
    
print("Number Guess: Dice Sum=", total_dice, "Player's Guess=", guess,"Points Recieved=", points )
    

  