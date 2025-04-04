#Importing module
import datetime

#Funtion to printing results
def Result(player_moves,computer_moves,player_holes,computer_holes,player,computer):
    print("\nHuman")
    print("Total Number Of Moves",player_moves)
    print("Total Number Of Balck Hole Hits",player_holes)
    print(player)
    print("\nComputer")
    print("Total Number Of Moves",computer_moves)
    print("Total Number Of Black Hole Hits",computer_holes)
    print(computer)

#Write results to text a file by using date and time
def ResultText(player_moves,computer_moves,player_holes,computer_holes,player,computer):
    now = datetime.datetime.now()
    CreateFile = now.strftime("%Y_%m_%d_%H_%M.txt")

    #Converting variables to string
    PlayerMoves=str(player_moves)
    PlayerHoles=str(player_holes)
    ComputerMoves=str(computer_moves)
    ComputerHoles=str(computer_holes)

    #Opening a text file in write mode
    with open(CreateFile,'w') as TEXT:
        TEXT.write("Human\n")
        TEXT.write(f"Total Number Of Moves {PlayerMoves}\n")
        TEXT.write(f"Total Number Of Black Hole Hits {PlayerHoles}\n{player}\n")
        TEXT.write("\nComputer\n")
        TEXT.write(f"Total Number Of Moves {ComputerMoves}\n")
        TEXT.write(f"Total Number Of Black Hole Hits {ComputerHoles}\n{computer}\n")

