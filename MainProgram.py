#Importing packages and modules
import time
import datetime
import random
from prettytable import PrettyTable
import rules 
import final.results as result

#Creating the header of the game board
def Header():
    block = 1
    while block <= 20:
        if block <10:
            print(" ", block, end=" ")
            block += 1
        else:
            print(" " + str(block), end=" ")
            block += 1
    print()

#Creating the 20*2 game board
def GameGrid():
    grid = PrettyTable()
    grid.header = False
    grid.add_row(player_list)
    grid.hrules = True
    grid.add_row(computer_list)

    Header()
    print(grid)
    return grid

while True:
    try:
        #Getting player name and welcoming to game
        player_name=input("Enter The Player Name : ")
        int(player_name)
        print("Invalid Input!, Try Again")
    except ValueError:
        print("\nHello",player_name,"You Are Welcome To The 20*2 Game!")
        break
    
#Creating the Lists
player_list = [" ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " "]
computer_list = [" ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " "]
#Creating and initializing variables
player_moves=0
computer_moves=0
player_holes=0
computer_holes=0
# main program
rules.Rules()
while True:
    #Declaring variables
    p1_player=0
    p2_computer=0
    #Human dice roll
    input("Roll The Dice (PRESS ENTER)\n")
    print("Rolling The Player Dice")
    human_dice=random.randint(1,6)
    print("You Rolled",human_dice)
    time.sleep(0.5)

    #Computer dice roll
    print("\nComputer Is Rolling The Dice")
    computer_dice=random.randint(1,6)
    print(f"Computer Rolled {computer_dice}\n")
    if human_dice==6:
        print(f"You Rolled {human_dice} And Can Start The Game")
        player_list[0]='X'
        GameGrid()
        time.sleep(0.5)
        print("\nYou Have Entered The Game And Current Location Is 1\n")
        while True:

            #Lists
            player_list = [" ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " "]
            computer_list = [" ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " "]
            #Rolling the human dice
            input("Roll The Dice (PRESS ENTER)\n")
            human_dice1=random.randint(1,6)
            if human_dice1!=0 : player_moves+=1
            print("Rolling The Player Dice")
            print('You Rolled',human_dice1)
            p1_player=p1_player+int(human_dice1/2)
            #Checking whether human hit a blackhole 
            if p1_player == 6 or p1_player == 13:
                p1_player=0
                print("\nYou Landed On A Black Hole And Moving Back To Block 1\n")
                player_holes+=1
            elif p1_player>=19:
                player_list[19]='X'
                #printing grid
                GameGrid()
                #Human wining the game
                print("\nCongratulations! You Won The Game\n")
                computer="Lost The Game"
                player="Congratulations! Won The Game"
                break
            player_list[p1_player]='X'
            if computer_dice!=6:
                time.sleep(0.5)
                #Rolling the computer dice
                print("\nComputer Is Rolling The Dice")
                computer_dice=random.randint(1,6)
                print(f"Computer Rolled {computer_dice}\n")
                #Checking whether computer can start the game
                if computer_dice==6:
                    print(f"\nComputer Rolled {computer_dice} And Can Start The Game")
                    player_list[0]='X'
                else:
                    print(f"\nComputer Rolled {computer_dice} And Cannot Start The Game")
            elif computer_dice==6:
                time.sleep(0.5)
                #Rolling the computer dice
                print("\nComputer Is Rolling The Dice")
                computer_dice1=random.randint(1,6)
                #Moving computer positions
                if computer_dice1!=1 : computer_moves+=1
                print("Computer Rolled",computer_dice1)
                p2_computer=p2_computer+int(computer_dice1/2)
                #Checking whether computer hit a blackhole
                if p2_computer == 6 or p2_computer == 13:
                    p2_computer=0
                    print("\nComputer Landed On A Black Hole And Moving Back To Block 1\n")
                    computer_holes+=1
                elif p2_computer>=19:
                    computer_list[19]='X'
                    #Printing grid
                    GameGrid()
                    #Computer wining the game
                    computer="Won The Game"
                    player="Oops! You Lost The Game"
                    print("\nComputer Won The Game\n")
                    break
                computer_list[p2_computer]='X'
            #Printing the grid
            GameGrid()
        #Calling the funtion to print the reult and write the result to text file
        result.Result(player_moves,computer_moves,player_holes,computer_holes,player,computer)
        result.ResultText(player_moves,computer_moves,player_holes,computer_holes,player,computer)
        #Restrting the game if the user want
        question=input("Do You Want To Play Again? (Yes/No) :").lower()
        if question == 'yes':
            print("You Reloded The Game")
            continue
        else:
            print("Game quitted")
            break
    #Checking whether computer can start the game
    elif computer_dice==6:
        print(f"Computer Rolled {computer_dice} And Can Start The Game")
        computer_list[0]='X'
        #Printing game grid
        GameGrid()
        time.sleep(0.5)
        print("\nComputer Have Entered The Game And Computer Location Is 1\n")
        while True:
            #Lists
            player_list = [" ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " "]
            computer_list = [" ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", " "]
            #Rolling the human dice
            if human_dice!=6:
                input("Roll The Dice (PRESS ENTER)\n")
                human_dice=random.randint(1,6)
                print("Rolling The Player Dice")
                print("You Rolled",human_dice)
                #Checking whether human can start the game
                if human_dice==6:
                    print(f"\nYou Rolled {human_dice} And Can Start The Game")
                    player_list[0]='X'
                else:
                    print(f"\nYou Rolled {human_dice} And Cannot Start The Game")
            #Rolling the human dice
            elif human_dice==6:
                input("Roll The Dice (PRESS ENTER)\n")
                human_dice1=random.randint(1,6)
                print("Rolling The Player Dice")
                print("You Rolled",human_dice1)
                #Moving the player positions
                if human_dice1!=1 : player_moves+=1
                p1_player=p1_player+int(human_dice1/2)
                #Checking the whether human hit a blackhole
                if p1_player == 6 or p1_player == 13:
                    p1_player=0
                    print("\nYou Landed On A Black Hole And Moving Back To Block 1\n")
                    player_holes+=1
                elif p1_player>=19:
                    player_list[19]='X'
                    #Printing the grid
                    GameGrid()
                    #Human won the game
                    print("\nCongratulations! You Won The Game\n")
                    computer="Lost the game"
                    player="Congratulations! Won the game"
                    break
                player_list[p1_player]='X'
            time.sleep(0.5)
            #Rolling computer dice
            print("\nComputer Is Rolling The Dice")
            computer_dice1=random.randint(1,6)
            print(f"Computer Rolled {computer_dice1}")
            #Moving the computer positions
            if computer_dice1!=1 : computer_moves+=1
            p2_computer=p2_computer+int(computer_dice1/2)
            #Checking whether computer hit the blackhole
            if p2_computer == 6 or p2_computer == 13:
                p2_computer=0
                print("\nComputer Landed On A Black Hole And Moving Back To Block 1\n")
                computer_holes+=1
            elif p2_computer>=19:
                computer_list[19]='X'
                #Computer wining the game
                print("\nComputer Won The Game\n")
                GameGrid()
                computer="Won The Game"
                player="Oops! You Lost The Game"
                break
            computer_list[p2_computer]='X'
            #Printing the grid
            GameGrid()
        #Calling the funtion to print the reult and write the result to text file
        result.Result(player_moves,computer_moves,player_holes,computer_holes,player,computer)
        result.ResultText(player_moves,computer_moves,player_holes,computer_holes,player,computer)
        #Replay the game if the user want
        question=input("Do You Want To Play Again? (Yes/No) :").lower()
        if question == 'yes':
            print("You Reloded The Game")
            continue
        else:
            print("Game quitted")
            break
    else:
        print(f"\nYou Rolled {human_dice} And Cannot Start The Game")
        print(f"Computer Rolled {computer_dice} And Cannot Start The Game\n")
        continue
