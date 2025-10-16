"""This program creates functions to implement three games which the user can 
play multiple times with the computer and keep track of their final score."""

import random

#### Game-1 Number Guess
def play_number_guess(guess) :
    '''Scoring points based on how close the user_guess is to the randomly generated sum of 2 dice'''
    dice1 = random.randint(1,6) 
    dice2 = random.randint(1,6) 
    total_dice = dice1 + dice2  
    points = 0
    
    #### calculating points
    if guess == total_dice:
       points = 10 # correct guess
    elif abs(total_dice - guess) <= 2:
       points = 5 # guess in the range of 2 from correct answer
    elif abs(total_dice - guess) <= 4:
       points = 1 # guess in the range of 4 from correct answer
    else: # every other wrong guess
       points =  0
    
    #### output
    print("Game = Number Guess, Dice Sum =", total_dice, ", Player's Guess =", guess,", Points Recieved =", points )
    
    return points

   


#### Game-2 modified rock, paper, scissor, lizard, spock
def play_mrpsls(move):
    '''plays mrpsls using the following inputs: (1 = "Rock", 2 = "Paper", 3 = "Scissor", 4 = "Lizard", 5 = "Spock")'''
    points_2 = 0
    bot = random.randint(1,5)
    
    # makes sure that user inputs a value between 1 and 5
    while move < 1 or move > 5:
        print("Error! please try again")
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
      
# calculating the winner
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
        points_2 = 10 # for user winning
    else:
        points_2 = 0 # for user loosing
    
    #### output
    print("Game = RPSLS, User =", user_move, ", Bot =", bot_move,",  Points recieved = ", points_2)     
    
    return points_2 

# Game-3 coin flip game
def play_coin():
    '''scoring points based based on randomly generated inputs'''
    flip1 = random.randint(0,1) # 0= tails, 1= heads
    points_3 = 0
    heads_count = 0
    
    # to give name to 0 and 1
    if flip1 == 1:
        first_flip = "Heads"
    else:
        first_flip = "Tails"
    
    print("Game = Coin Flip, Flip =", first_flip, end="")
    
     #### points calculation
    if flip1 == 0:
        
         # second flip and gives name to 0 and 1
        flip = random.randint(0,1)
        if flip == 1:
            next_flip =  "Heads"
        else:
            next_flip =  "Tails"
        print(", ", next_flip, end="")
        
         # loop till the time flip 2 = heads 
        while flip == 1:
            points_3 = points_3 + 2 # adds 2 points 
            
             # flips till the time heads is generated and then adds 2 points
            flip = random.randint(0,1)
            if flip == 1:
                next_flip =  "Heads"
            else:
                next_flip =  "Tails"
            print(", ", next_flip, end="")
    else: # when first flip is heads
        while heads_count < 2: # loops till the time 2 more heads are not generated
              # flips and assignes name to 0 and 1 for printing
             flip = random.randint(0,1)
             if flip == 1:
                 next_flip =  "Heads"
             else:
                 next_flip =  "Tails"
             print(", ", next_flip, end="")
             
             if flip == 1:# if flip is heads = adds 1 to heads_count
                 heads_count = heads_count + 1
                 
             if flip == 0: # if flip is tails adds 1 to points
                 points_3 = points_3 + 1
    print("; Total points = ", points_3)
    return points_3   


#### gamer room    
def games_room(name) :
    '''Lets the user play the game of their choice and keeps track of cummulative score'''
    score = 0
    print()
    print("Hello,", name, "! Welcome to the Games Room") #greets user
    while True: #infinite loop to ask user for what game to play after every game and keep track of cummulative score
        print()
        print("Your current score is", score)
        print()
        print("Enter 1 for Number Guess, 2 for RPSLS, 3 for Coin Flip and 4 for Quit")
        choice = int(input("What game do you want to play? ")) 
        if choice == 1: 
            guess= int(input("Enter your guess:"))
            score = score + play_number_guess(guess) # to add points achieved in the game to cummulative score
        elif choice == 2:
            print()
            print("Enter 1 for Rock, 2 for Paper, 3 for Scissor, 4 for Lizard and 5 for spock.")
            move = int(input("Enter your move:"))
            score = score + play_mrpsls(move) # to add points achieved in the game to cummulative score
        elif choice == 3: 
            print()
            score = score + play_coin() # to add points achieved in the game to cummulative score
        elif choice == 4:  
            print()
            print("Thank you for playing! Your Score is : ", score)
            break #exits the loop
        else: # if user input is not between 1-4, points get deducted
            points_lost = random.randint(1,5)
            score = score - points_lost
            print("ERROR! wrong choice you lost", points_lost, "points, total score is", score)
           
# Main Program
name=str(input("what is your name?")) 
games_room(name)