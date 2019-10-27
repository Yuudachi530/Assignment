import random
Grid = {}
Points = [0, 0]
GameEnd = False


def SetUpEmptyGrid():
    for i in range(1, 8 + 1):
        for j in range(1, 8 + 1):
            Grid[i, j] = 0

def GetEmptyGridPosition():
    while True:
        global x, y
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        if Grid[x, y] == 0:
            break

def RandomlyDistributeCards():
    for Number in range(1, 32 + 1):
        GetEmptyGridPosition()
        Grid[x, y] = Number
        GetEmptyGridPosition()
        Grid[x, y] = Number
        
def SetUpPlayers():
    global ThisPlayer
    Points[1 - 1] = 0
    Points[2 - 1] = 0
    ThisPlayer = 1 - 1
    
def DisplayGrid():
    for i in range(1, 8 + 1):
        print()
        for j in range(1, 8 + 1):
            if i == x1 and j == y1:
                print(' ', Grid[i, j], ' ', end = '')
            elif Grid[i, j] == 0:
                print('    ', end = '')
            else:
                print(' ', '?', ' ', end = '')
    
def GetPlayersCoordinates():
    global x1, y1, x2, y2
    while True:
        x1, y1 = int(input('enter the coordinate: ')), int(input())
        if Grid[x1, y1] > 0:
            break
    DisplayGrid()
    while True:
        x2, y2 = int(input('enter the coordinate: ')), int(input())
        if Grid[x2, y2] != 0  and (( x2 != x1 and y1 == y2) or (x2 == x1 and y1 == y2)):
            break

def SwapPlayers():
    global ThisPlayer
    if ThisPlayer == 1 - 1:
        ThisPlayer = 2 - 1
    elif ThisPlayer == 2 - 1:
        ThisPlayer = 1 - 1
    
     
def TestForMatch():
    if Grid[x1, y1] == Grid[x2, y2]:
        Grid[x1, y1] = ''   
        Grid[x2, y2] = ''
        Points[ThisPlayer - 1] = Points[ThisPlayer - 1] + 1
    else:
        SwapPlayers()
        
def TestForEndGame():
    global GameEnd
    if Points[1 - 1] + Points[2 - 1] == 32:
        GameEnd = True
        
def OutputResults():
    if Points[0] > Points[1]:
        print('player1 wins')
    elif Points[1] > Points[0]:
        print('player2 wins')
    else:
        print('draw')
    
#main program
SetUpEmptyGrid()
RandomlyDistributeCards()
SetUpPlayers()
GameEnd = False
while True:
     GetPlayersCoordinates()
     DisplayGrid()
     TestForMatch()
     TestForEndGame()
     if GameEnd == True:
         break
OutputResults()
     
     
     
     
     
    


        

            




