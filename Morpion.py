import random


nom = input("veuillez saisir votre nom : ")


def initGame():
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    currentPlayer = "X"
    gameRunning = True
    return board, currentPlayer, gameRunning

# installation du tableau de jeu

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])





# Création d'un joueur

def PlayerInput(board, currentPlayer):
    inp = int(input("entrer un nombre entre 1 et 9 :"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
        return board
    else:
        print("Cette zone est déjà utilisé, veuillez en choisir une autre")
        return PlayerInput(board, currentPlayer)

# vérification victoire ou égalité

def horizontal(board):
    if board[0] == board[1] == board [2] and board[1] != "-":
        winner = board[0]
        return winner
    elif board[3] == board[4] == board [5] and board[3] != "-":
        winner = board[3]
        return winner
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return winner
    return False

def vertical(board):
    if board[0] == board[3] == board [6] and board[0] != "-":
        winner = board[0]
        return winner
    elif board[1] == board[4] == board [7] and board[1] != "-":
        winner = board[1]
        return winner
    elif board[2] == board[5] == board [8] and board[2] != "-":
        winner = board[2]
        return winner
    return False

def diago(board):
    if board[0] == board[4] == board [8] and board[0] != "-":
        winner = board[0]
        return winner
    elif board[2] == board[4] == board [6] and board[2] != "-":
        winner = board[2]
        return winner
    return False

def égalité(board):
    if "-" not in board:
        printBoard(board)
        print("EGALITE")
        return True
    return False


def vérifWin(board):
    if horizontal(board) == "X" or vertical(board) == "X" or diago(board) == "X":
        print("La victoire appartient à ", nom)
        return True
    elif horizontal(board) == "O" or vertical(board) == "O" or diago(board) == "O":
        print("La victoire appartient à IA")
        return True
    return False

# changement de joueur
def changement(currentPlayer):
    if currentPlayer == "X":
        currentPlayer = "O"
    else :
        currentPlayer = "X"
    return currentPlayer


# IA
def IA(board, currentPlayer):
    while currentPlayer == "O":
        position = random.randint (0,8)
        if board[position] == "-" :
            board[position] = "O"
            currentPlayer = changement(currentPlayer)
    return currentPlayer, board


def game():
    board, currentPlayer, gameRunning = initGame()
    while gameRunning :
        printBoard(board)
        board = PlayerInput(board, currentPlayer)
        check = vérifWin(board)
        if check:
            gameRunning = False
            break
        check = égalité(board)
        if check:
            gameRunning = False
            break
        currentPlayer = changement(currentPlayer)
        currentPlayer, board = IA(board, currentPlayer)
        check = vérifWin(board)
        if check:
            gameRunning = False
            break
    
    rematch = input("voulez-vous rejouez ? (o, n)")

    if rematch.lower() == "o":
        game()
    else :
        print("Fin du jeu")

game()