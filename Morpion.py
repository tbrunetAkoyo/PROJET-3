import random
from random import randrange

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
    id_win = verifCloseWin(board, currentPlayer)
    real_player = changement(currentPlayer)
    id_lose = verifCloseWin(board, real_player)
    if id_win:
        board[id_win] = currentPlayer
    elif id_lose:
        board[id_lose] = currentPlayer
    else:
        if verifCentre(board):
            board[4] = currentPlayer
        # elif vérification si un pion est déjà posé de l'ia. Si oui vérifié comme commenter en dessous
        # si non entrer dans vérifCorner.
        elif verifCorner(board):
            not_put = 1
            list_corner = [0, 2, 6, 8]
            while not_put == 1:
                random_position = list_corner.pop(randrange(len(list_corner)))
                if board[random_position] == '-':
                    board[random_position] = currentPlayer
                    not_put = 0

# Il va falloir regarder si tu as la possibilité de poser sur une diagonal où aucun pion enemi n'est posé.
# Faire la même chose pour les verticales et horizontales

# Privilégié les diagonales


    currentPlayer = changement(currentPlayer)
    # while currentPlayer == "O":
    #     position = random.randint (0,8)
    #     if board[position] == "-" :
    #         board[position] = "O"
    #         currentPlayer = changement(currentPlayer)

    return currentPlayer, board

def verifCentre(board):
    if board[4] == '-':
        return True
    return False

def verifCorner(board):
    if '-' in (board[0], board[2], board[6], board[8]):
        return True
    return False


def verifDiagoWin(board, player):
    diago1 = {0: board[0], 4: board[4], 8: board[8]}
    diago1_list = [board[0], board[4], board[8]]

    diago2 = {2: board[2], 4: board[4], 6: board[6]}
    diago2_list = [board[2], board[4], board[6]]

    if diago1_list.count(player) == 2:
        for key, value in diago1.items():
            if value == '-':
                return key
    elif diago2_list.count(player) == 2:
        for k, v in diago2.items():
            if v == '-':
                return k

def verifVerticalWin(board, player):
    vertical1 = {0: board[0], 3: board[3], 6: board[6]}
    vertical1_list = [board[0], board[3], board[6]]

    vertical2 = {1: board[1], 4: board[4], 7: board[7]}
    vertical2_list = [board[1], board[4], board[7]]

    vertical3 = {2: board[2], 5: board[5], 8: board[8]}
    vertical3_list = [board[2], board[5], board[8]]

    if vertical1_list.count(player) == 2:
        for k, v in vertical1.items():
            if v == '-':
                return k
    elif vertical2_list.count(player) == 2:
        for k, v in vertical2.items():
            if v == '-':
                return k
    elif vertical3_list.count(player) == 2:
        for k, v in vertical3.items():
            if v == '-':
                return k

def verifHorizontalWin(board, player):
    horizontal1 = {0: board[0], 1: board[1], 2: board[2]}
    horizontal1_list = [board[0], board[1], board[2]]

    horizontal2 = {3: board[3], 4: board[4], 5: board[5]}
    horizontal2_list = [board[3], board[4], board[5]]

    horizontal3 = {6: board[6], 7: board[7], 8: board[8]}
    horizontal3_list = [board[6], board[7], board[8]]

    print(horizontal1_list)
    if horizontal1_list.count(player) == 2:
        for k, v in horizontal1.items():
            if v == '-':
                return k
    elif horizontal2_list.count(player) == 2:
        for k, v in horizontal2.items():
            if v == '-':
                return k
    elif horizontal3_list.count(player) == 2:
        for k, v in horizontal3.items():
            if v == '-':
                return k


def verifCloseWin(board, player):
    id_diago = verifDiagoWin(board, player)
    if id_diago:
        return id_diago
    id_vertical = verifVerticalWin(board, player)
    if id_vertical:
        return id_vertical
    id_horizontal = verifHorizontalWin(board, player)
    if id_horizontal:
        return id_horizontal
    
    

# vérification de nouvelle victoire ou égalité 

def game():
    board, currentPlayer, gameRunning = initGame()
    while gameRunning:
        # Print board pour savoir où la partie en est.
        # Pour que le joueur sache où il peut poser
        printBoard(board)
        # Tour du player
        board = PlayerInput(board, currentPlayer)
        check = vérifWin(board)
        if check:
            gameRunning = False
            printBoard(board)
            break
        check = égalité(board)
        if check:
            gameRunning = False
            printBoard(board)
            break

        # Changement de joueur à l'IA
        currentPlayer = changement(currentPlayer)

        # Tour de l'IA et passage au joueur
        currentPlayer, board = IA(board, currentPlayer)
        check = vérifWin(board)
        if check:
            gameRunning = False
            printBoard(board)
            break
    
    rematch = input("Voulez-vous rejouer ? (o, n)")
    if rematch.lower() == "o":
        game()
    else:
        print("Fin du jeu.")

game()