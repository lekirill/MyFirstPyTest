import random


def initField():
    for i in range(3):
        field.append([])
        for j in range(3):
            field[i].append('*')

def printField():
    for i in field:
        print(i)
    print("---------")


def makeMove(player, g):
    correct_move = False
    g = g
    if g:
        while not correct_move:
            if player == 'X':
                x = int(input('Insert the point\'s X: '))
                y = int(input('Insert the point\'s Y: '))
            else:
                x, y = random.randint(0,2), random.randint(0,2)

            if field[x][y] == "*":
                field[x][y] = player
                printField()
                correct_move = True


def winCheck(player, g):
    g = g
    won = None
    if (field[0][0] == field[0][1] == field[0][2] == player or \
       field[0][0] == field[1][1] == field[2][2] == player or \
       field[0][0] == field[1][0] == field[2][0] == player or \
       field[0][1] == field[1][1] == field[2][1] == player or \
       field[0][2] == field[1][2] == field[2][2] == player or \
       field[0][2] == field[1][1] == field[2][0] == player or \
       field[2][0] == field[2][1] == field[2][2] == player or \
       field[1][0] == field[1][1] == field[1][2] == player) and g == True:
        g = False
        print(player + " has won!")
        won = player
    return g, won


def playGame():
    g = gaming
    initField()
    printField()
    while g:
        if g:
            makeMove(players[0], g)
            g, won = winCheck(players[0], g)
        if g:
            makeMove(players[1], g)
            g, won = winCheck(players[1], g)
    return won

field=[]
players = ('X', 'O')
gaming = True


winner = playGame()
print("The game is finished! The winner is " + winner)