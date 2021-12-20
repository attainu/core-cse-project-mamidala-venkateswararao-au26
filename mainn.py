position=0
print("press r to roll")
print("press q to quite")
import random      # import random labrary
def roll(position):
    inp=str(input())
    while inp!="q":   # while loop for proceesing for untill the user win
        x=random.randint(1,6)
        if x==1:          # assigning different positions for different dice values
            position+=1
        if x==2:
            position+=2
        if x==3:
            position+=3
        if x==4:
            position+=4
        if x==5:
            position+=5
        if x==6:
            position+=6   
        print("The dice rollerd ",x,"step forward") 

        print("You are At ",position)
        if position==1:
            position=38
        if position==28:
            position=77
        if position==21:
            position=42
        if position==71:
            position=92
        print("U Got a Ludder, Lucky!")   
        if position==32:
            position=10
        if position==36:
            position=6
        if position==62:
            position=18
        if position==95:
            position=56  
        print("OOPS! IT's A snake") 

        if position==100:
            print("Congratulation You win!") 
            break 
        if position<100:
            print("Due to promotion ,ur currun Positipn is;",position)  
        if position>100:
            print("imposible to move!")     
            continue



obj=roll(position)  



################### 2nd Method ##################3

"""import random

player=[0,0]   # player 1, player 2 they start with 0
i=0
print("WelCome")
print("Snake Ladder")
print("Game Begins")
#print("position 1,21,28,71 are ladders")
#print("position 10,25,38,48 are Snakes ")

def roll(i):
    while(player[0]!=100 and player [1]!=100):  #player are not in 100 then loop will run countunly
        print("player",i+1,"turn")
        player[i]+=random.randint(1,6)   # player[i]=player[i]+random.randint(1,6)
        if (player[i]==1 or player[i]==28 or player[i]==21 or player[i]==71):

            print("Lucky! Got a ladder")
            if player[i]==1:
                player[i]=38
            if player[i]==28:
                player[i]=77
            if player[i]==21:
                player[i]=42
            if player[i]==71:
               player[i]=92 
        if (player[i]==32 or player[i]==36 or player[i]==62 or player[i]==95):    
            print("OOPS! IT's A snake")  
            if player[i]==32:
                player[i]=10
            if player[i]==36:
                player[i]=6
            if player[i]==62:
                player[i]=18
            if player==95:
                player[i]=56  
        i=(i+1)%2

        if (player[i]==100):
            print("Congratulations",player[i])
            break
        

obj=roll(0)"""        




    







