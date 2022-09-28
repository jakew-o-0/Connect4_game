def check_horizontal(pos, player):
    isOne = 0
    ########: itterates through the whole sublist if there are four the same than true is returned 
    for i in range(len(grid[pos])):
        if(grid[pos][i] == int(player)):
            isOne += 1
        if(isOne == 4):
                return True
        elif(isOne != 4 and i == len(grid[pos])):
           return False

def check_vertical(pos, player):
    isOne = 0
    ########: itterates through all sublists checking only a specific item in every sublist if there are four the same true is returned
    for i in range(len(grid[pos])):
        if(grid[i][pos] == int(player)):
            isOne += 1
        if(isOne == 4):
            return True
        elif(isOne != 4 and i == len(grid[pos])):
           return False

def check_diagonal(pos, player):
    ########: itterates diagonaly up and right if there is a one or a two(depending on the player) isOne is incremented by one
    try:
        isOne = 0
        for i in range(4):
            if(grid[pos[0] - i][pos[1] + i] == player):
                isOne += 1
        if(isOne == 4):
            return True       
    ########: itterates diagonaly down and left, same as above
    except(IndexError):
        try:
            isOne = 0
            for i in range(4):
                if(grid[pos[0] + i][pos[1] - i] == player):
                    isOne += 1
            if(isOne == 5):
                return True

        except(IndexError):
            pass 
                        
    ########: iterates diagonaly up and left
    try:
        isOne = 0
        for i in range(4):
            if(grid[pos[0] + i][pos[1] + i] == player):
                isOne += 1
        if(isOne == 4):
            return True       
    ########: itterates diagonaly down and right, same as above
    except(IndexError):
        try:
            isOne = 0
            for i in range(4):
                if(grid[pos[0] - i][pos[1] - i] == player):
                    isOne += 1
            if(isOne == 4):
                return True
        except(IndexError):
            pass 

def set_grid():
    ########: sets the size of the grid between 4 and 10 apon user input && input sanitation
    while(True):
        try:
            grid = int(input("size of grid?\n(4-10)"))
            if(grid >= 4 and grid <=10):
                ########: fills a 2d list of 0's to the size of the input number
                g = [[0,] * grid] * grid
                return g
            else:
                print("Too big")
        except(TypeError):
            print("not a number")

def main():

    isPlayerOne = False
    grid = set_grid()

    while(True):
        ########: the user is changed between player 1 and 2 with each itteration
        isPlayerOne = not(isPlayerOne)
        if(isPlayerOne):
            player = 1
        else:
            player = 2
        
        ########: prints the grid and gets the user input
        for i in range(len(grid)):
            print(grid[i])
        usrIn = int(input("what column, player {}\n(0-{}): ".format(player, len(grid) - 1)))

        ########: places the players number in the correct spot in the grid
        ########: itterates through the 2d list for nth position in the sublist
        ########: if the item is not 0 then the item in the previous sublist is changed to the players number
        ########: else the loop has gotten to the bottom of the list so that means its empty and so it is changed to the players number
        for i in range(len(grid)):
            if(grid[i][usrIn] != 0):
                grid[i - 1][usrIn] = int(player)
                i = i - 1
                break
            elif(i == 3):
                grid[i][usrIn] = player

        ########: after each player takes a turn the game is checked for winning conditions; at the position of the current play
        if(check_horizontal(i, player) or check_vertical(usrIn, player) or check_diagonal(pos=(i,usrIn), player=player)):
            print("4 in a row")
            break

if(__name__ == "__main__"):
    main()