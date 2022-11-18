import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
nom = input("veuillez saisir votre nom : ")
currentPlayer = "X"
winner = None
gameRunning = True

# installation du tableau de jeu

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)


# Création d'un joueur

def PlayerInput(board):
    inp = int(input("entrer un nombre entre 1 et 9 :"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Cette zone est déjà utilisé, veuillez en choisir une autre")
        return inp

# vérification victoire ou égalité

def horizontal(board):
    global winner
    if board[0] == board[1] == board [2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board [5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True

def vertical(board):
    global winner
    if board[0] == board[3] == board [6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board [7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board [8] and board[2] != "-":
        winner = board[2]
        return True

def diago(board):
    global winner
    if board[0] == board[4] == board [8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board [6] and board[2] != "-":
        winner = board[2]
        return True

def égalité(board):
    if "-" not in board:
        printBoard(board)
        print("EGALITE")
        gameRunning = False


def vérifWin():
    if horizontal(board) or vertical(board) or diago(board) == "X":
        print("La victoire appartient à ", nom)
    else:
        print("La victoire appartient à IA")

# changement de joueur
def changement():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else :
        currentPlayer = "X"


# IA
def IA(board):
    while currentPlayer == "O":
        position = random.randint (1,9)
        if board[position] =="-":
            board[position] = "O"
            changement()

# vérification de nouvelle victoire ou égalité 

while gameRunning:
    printBoard(board)
    PlayerInput(board)
    vérifWin()
    égalité(board)
    changement()
    IA(board)
    vérifWin()
    égalité(board)
while