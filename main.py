import pygame
from pawn import Pawn
from king import King
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight

# Variables and other essentials
SCREEN_SIZE = 640
PIECE_SIZE = 80
board = [[None for i in range(0,8)] for k in range(0,8)]
selected_coin = [1,0]
current_player = 1
in_check_ = False
in_checkopp_ = False
kingW = [7,3]
kingB = [0,3]
move_log = []
destionations = []

# Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE, 720))
pygame.display.set_caption("Chess Game")
icon = pygame.image.load(r'./images/icon.png')
pygame.display.set_icon(icon)
chessBoard = pygame.image.load('./images/chessBoard.jpg')
font = pygame.font.SysFont(pygame.font.get_fonts()[20], 32)
fontIn = pygame.font.SysFont(pygame.font.get_fonts()[10], 25)

def get_all_moves(color):
    all = []
    for i, ii in enumerate(board):
        for j, jj in enumerate(ii):
            if jj != None:
                if jj.color == color:
                    all += jj.find_destinations(board)[1]
    return all


def in_check(checkFor):
    global kingB,kingW
    all = get_all_moves(not checkFor)
    pos = kingB if checkFor == 0 else kingW
    for i in all:
        if i.pos == pos:
            return True


def _in_check_sub(checkFor):
    pos = kingB if checkFor == 0 else kingW
    squareUnderCheck(checkFor,pos)


def squareUnderCheck(checkFor,pos):
    oppmoves = get_all_moves(not checkFor)
    for i in oppmoves:
        if i.pos == pos:
            return True

    return False

def undo_move():
    global board,destionations,current_player
    destionations = []
    if not move_log:
        print("No more Undos!")
    else:
        board = move_log[-1].undo_pos(board)
        move_log.pop()
        current_player = not current_player

def make_board():
    def add_coin(type,pos,gridcolor=-1):
        k,l = pos
        x = l * PIECE_SIZE
        y = k * PIECE_SIZE
        rectB = pygame.Rect(x, y, PIECE_SIZE, PIECE_SIZE)
        switcher ={
            "PawnB": Pawn((k, l), 0, 0, rectB, pygame.image.load('./images/pawnBlack.png')),
            "PawnW": Pawn((k, l), 1, 0, rectB, pygame.image.load('./images/pawnWhite.png')),
            "RookB": Rook((k, l), 0, 0, rectB, pygame.image.load('./images/RookBlack.png')),
            "RookW": Rook((k, l), 1, 0, rectB, pygame.image.load('./images/RookWhite.png')),
            "KnightB": Knight((k, l), 0, 0, rectB, pygame.image.load('./images/KnightBlack.png')),
            "KnightW": Knight((k, l), 1, 0, rectB, pygame.image.load('./images/KnightWhite.png')),
            "BishopB": Bishop((k, l), 0, 0, rectB, pygame.image.load('./images/BishopBlack.png'),gridcolor),
            "BishopW": Bishop((k, l), 1, 0, rectB, pygame.image.load('./images/BishopWhite.png'),gridcolor),
            "QueenB": Queen((k, l), 0, 0, rectB, pygame.image.load('./images/QueenBlack.png')),
            "QueenW": Queen((k, l), 1, 0, rectB, pygame.image.load('./images/QueenWhite.png')),
            # Not Done
            "KingB": King((k, l), 0, 0, rectB, pygame.image.load('./images/KingBlack.png')),
            "KingW": King((k, l), 1, 0, rectB, pygame.image.load('./images/KingWhite.png'))

        }

        return switcher.get(type,None)
    # Pawns
    for i in range(0,8):
        board[1][i] = add_coin("PawnB",[1,i])
    for i in range(0,8):
        board[6][i] = add_coin("PawnW",[6,i])
#   Kings
    board[0][3] =  add_coin("KingB",[0,3])
    board[7][3] =  add_coin("KingW",[7,3])
#   Queens
    board[0][4] =  add_coin("QueenB",[0,4])
    board[7][4] =  add_coin("QueenW",[7,4])
#   Rooks
    board[0][0] =  add_coin("RookB",[0,0])
    board[0][7] =  add_coin("RookB",[0,7])
    board[7][7] =  add_coin("RookW",[7,7])
    board[7][0] =  add_coin("RookW",[7,0])

#   Knights
    board[0][1] =  add_coin("KnightB",[0,1])
    board[0][6] =  add_coin("KnightB",[0,6])
    board[7][6] =  add_coin("KnightW",[7,6])
    board[7][1] =  add_coin("KnightW",[7,1])

#   Bishops
    board[0][2] =  add_coin("BishopB",[0,2],0)
    board[0][5] =  add_coin("BishopB",[0,5],1)
    board[7][5] =  add_coin("BishopW",[7,5],0)
    board[7][2] =  add_coin("BishopW",[7,2],1)

def blit_essentials():
    screen.blit(chessBoard,(0,0))

def blit_check(text):
    textIncorrect = fontIn.render(text, True, (0, 0, 0))
    textRectIncorrect = textIncorrect.get_rect()
    textRectIncorrect.center = (320, 710)
    screen.blit(textIncorrect,textRectIncorrect)

def blit_pieces_destinations():

    def draw_rect(selection):
        # rect = pygame.Rect(x+5, y+5, CoinSize-10, CoinSize-10)
        if selection.kill:
            s = pygame.Surface((70, 70))  # the size of your rect
            s.set_alpha(128)  # alpha level
            s.fill((217, 7, 24))
            screen.blit(s, selection.rectangle)
        elif selection.slant:
            s = pygame.Surface((70, 70))  # the size of your rect
            s.set_alpha(128)  # alpha level
            s.fill((3, 103, 166))
            screen.blit(s, selection.rectangle)
        else:
            s = pygame.Surface((70, 70))  # the size of your rect
            s.set_alpha(128)  # alpha level
            s.fill((3, 140, 62))
            screen.blit(s, selection.rectangle)

    for i in destionations:
        draw_rect(i)

    for i in board:
        for j in i:
            if j != None:
                screen.blit(j.image,j.rectangle)


def click_selected(pos):
    global selected_coin,current_player, board,destionations,move_log,kingB,kingW,in_check_,in_checkopp_

    for i, ii in enumerate(destionations):
        if ii.rectangle.collidepoint(pos) == True:
            kill = False
            if board[ii.pos[0]][ii.pos[1]] != None:
                kill = True
            if board[selected_coin[0]][selected_coin[1]].type == 'King':
                if board[selected_coin[0]][selected_coin[1]].color == 0:
                    kingB = [ii.pos[0],ii.pos[1]]
                else:
                    kingW = [ii.pos[0],ii.pos[1]]
            board,move = board[selected_coin[0]][selected_coin[1]].change_pos([ii.pos[0],ii.pos[1]],board,board[selected_coin[0]][selected_coin[1]],board[ii.pos[0]][ii.pos[1]],kill,False)
            move_log.append(move)
            destionations = []
            if in_check(current_player):
                print("if u move it will be under check")
                undo_move()
                in_check_ = True
                in_checkopp_ = False
            if not in_check_:
                if in_check(not current_player):
                    print(f'{"Black" if current_player == 0 else "White"}s made a check')
                    in_checkopp_ = True
                    in_check_ = False
                    current_player = not current_player
                else:
                    in_checkopp_ = False
                    in_check_ = False
                    current_player = not current_player
            else:
                in_check_ = False
                in_checkopp_ = False
                current_player = not current_player

            return True
    destionations = []
    return False

def find_clicked(pos):
    x,y =pos
    global selected_coin
    for i, ii in enumerate(board):
        for j, jj in enumerate(ii):
            if jj != None:
               if jj.rectangle.collidepoint(pos) == True:
                   if jj.color == current_player:
                        selected_coin = [i, j]
                        return True
                   else:
                       selected_coin = [-1,-1]
                       return False

    selected_coin = [-1, -1]
    return False


def blit_message(text):
    textIncorrect = fontIn.render(text, True, (0, 0, 0))
    textRectIncorrect = textIncorrect.get_rect()
    textRectIncorrect.center = (320, 670)
    screen.blit(textIncorrect,textRectIncorrect)


make_board()

incorrect = False
no_moves = False
running = True

while running:
    clock.tick(60)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sel = click_selected(event.pos)
            if not click_sel:
                clicked = find_clicked(event.pos)
                if clicked:
                    x,y = selected_coin
                    destionations,kill = board[x][y].find_destinations(board)
                    if not destionations:
                        textshowtime = pygame.time.get_ticks()
                        print("No moves!!")
                        no_moves = True


                else:
                    textshowtime = pygame.time.get_ticks()
                    print(f'{"Black" if current_player == 0 else "White"}s move')
                    incorrect = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                undo_move()


    currentTime = pygame.time.get_ticks()
    if incorrect:
        current = 'Black' if current_player == 0 else 'White'
        blit_message(f"{current}'s move")
        if currentTime - textshowtime > 2000:
            incorrect = False
    elif no_moves:
        blit_message("No Moves!")
        if currentTime - textshowtime > 2000:
            no_moves = False
    elif in_check_:
        blit_message("If you move you will be under check!")
    elif in_checkopp_:
        blit_check(f'{"Black" if not current_player == 0 else "White"} made check ')


    blit_essentials()
    blit_pieces_destinations()

    pygame.display.update()
