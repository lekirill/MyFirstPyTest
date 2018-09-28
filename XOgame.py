import random
move = random.randint(0, 100)
field=[]
players = ('X', 'O')
gaming = True


def initField():
    for i in range(3):
        field.append([])
        for j in range(3):
            field[i].append('*')

initField()
print(field)

def makeMove(player):
    if player == 'X':
        x, y = input('Insert the point\'s coordinates: ', x, y)
    else:
        x, y = random.randint(0,2), random.randint(0,2)
    if field[x][y] != '*':
        print('The cell is filled. Choose another one')
    else:
        field[x][y] = player


def playGame():
    while gaming:
        makeMove(players(1))
        makeMove(players(2))
def winCheck():
    if field[0][0] == field[0][1] == field[0][2] or \
       field[0][0] == field[1][1] == field[2][2] or \
       field[0][0] == field[1][0] == field[2][0] or \
       field[0][1] == field[1][1] == field[2][1] or \
       field[0][2] == field[1][2] == field[2][2] or \
       field[0][2] == field[1][1] == field[2][0] or \
       field[2][0] == field[2][1] == field[2][2] or \
       field[1][0] == field[1][1] == field[1][2]:
        gaming = False
