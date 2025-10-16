import random
print("Enter 1 for Rock, 2 for Paper, 3 for Scissor, 4 for Lizard and 5 for spock.")

points_2 = 0
bot = random.randint(1,5)
move = int(input("Enter your move:"))    
# giving name to the move of bot 

if bot == 1:
        bot_move =  "Rock"
elif bot == 2:
        bot_move =  "Paper"
elif bot == 3:
        bot_move =  "Scissor"
elif bot == 4:
        bot_move = "Lizard"
else:
        bot_move =  "Spock"

# giving name to the move of user         
if move == 1:
        user_move =  "Rock"
elif move == 2:
        user_move =  "Paper"
elif move == 3:
        user_move =  "Scissor"
elif move == 4:
        user_move = "Lizard"
else:
        user_move =  "Spock"
   
# if else satetments to caolculate who wins    
if move == bot:
        points_2 = 5 # for tie
elif (move == 1 and (bot == 5 or bot == 3)):
        points_2 = 10
elif (move == 2 and (bot == 1 or bot == 4)):
        points_2 = 10
elif (move == 3 and (bot == 2 or bot == 5)):
        points_2 = 10
elif (move == 4 and (bot == 3 or bot == 1)):
        points_2 = 10
elif (move == 5 and (bot == 4 or bot == 2)):
        points_2 = 10
else:
        points_2 = 0
print("RPSLS: User:", user_move, ", Bot:", bot_move,",  Points recieved: ", points_2)   

