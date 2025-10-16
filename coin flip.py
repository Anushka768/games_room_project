import random
def play_coin():
    flip1 = random.randint(0,1) # 0= tails, 1= heads
    points_3 = 0
    heads_count = 0
    if flip1 == 1:
        first_flip = "Heads"
    else:
        first_flip = "Tails"
    
    print("Coin Flip: Flip =", first_flip, end="")
    
    
    if flip1 == 0:
        flip = random.randint(0,1)
        if flip == 1:
            next_flip =  "Heads"
        else:
            next_flip =  "Tails"
        print(", ", next_flip, end="")
        while flip == 1:
            points_3 = points_3 + 2
            flip = random.randint(0,1)
            if flip == 1:
                next_flip =  "Heads"
            else:
                next_flip =  "Tails"
            print(", ", next_flip, end="")
    else:
        while heads_count < 2:
             flip = random.randint(0,1)
             if flip == 1:
                 next_flip =  "Heads"
             else:
                 next_flip =  "Tails"
             print(", ", next_flip, end="")
             
             if flip == 1:
                 heads_count = heads_count + 1
                 
             if flip == 0:
                 points_3 = points_3 + 1
    print(", Total points = ", points_3)
    return points_3   
play_coin()