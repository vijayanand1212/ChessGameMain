import pygame
from selection import Selection
from move import Move
class Pawn():
    def __init__(self, pos, color, coinindex, rectangle, image):
        self.pos = pos
        self.color = color
        self.coinIndex = coinindex
        self.rectangle = rectangle
        self.image = image
        self.type = "Pawn"

    def find_destinations(self, Board):
        dest = []
        kills = []
        x, y = self.pos
        if self.color == 0:
            kill = False
            try:
                if Board[x + 1][y - 1] != None and Board[x + 1][y - 1].color != self.color:
                    kill = True
                    dest.append(Selection([x + 1, y - 1], kill))
                    kills.append(Selection([x + 1, y - 1], kill))

            except:
                pass
            try:
                if Board[x + 1][y + 1] != None and Board[x + 1][y + 1].color != self.color:
                    kill = True
                    dest.append(Selection([x + 1, y + 1], kill))
                    kills.append(Selection([x + 1, y + 1], kill))

            except:
                pass
            try:
                if not kill:
                    if Board[x + 1][y] == None:
                        dest.append(Selection([x + 1, y], False))
                        if x == 1 and Board[x + 2][y] == None:
                            dest.append(Selection([x + 2, y], False))
            except:
                print("There is no Move")
        else:
            kill = False
            try:
                if Board[x - 1][y - 1] != None and Board[x - 1][y - 1].color != self.color:
                    kill = True
                    dest.append(Selection([x - 1, y - 1], kill))
                    kills.append(Selection([x - 1, y - 1], kill))

            except:
                pass
            try:
                if Board[x - 1][y + 1] != None and Board[x - 1][y + 1].color != self.color:
                    kill = True
                    dest.append(Selection([x - 1, y + 1], kill))
                    kills.append(Selection([x - 1, y + 1], kill))

            except:
                pass
            if not kill:
                if Board[x - 1][y] == None:
                    dest.append(Selection([x - 1, y], False))
                    if x == 6 and Board[x - 2][y] == None:
                        dest.append(Selection([x - 2, y], False))

        return dest,kills

    def change_pos(self, new_pos, Board,from_obj,kill_obj,kill,check):
        i, j = new_pos
        x = j * 80
        y = i * 80
        Board[i][j] = Board[self.pos[0]][self.pos[1]]
        Board[self.pos[0]][self.pos[1]] = None
        move = Move([self.pos[0],self.pos[1]],new_pos,from_obj,kill_obj,kill,check)
        rect = pygame.Rect(x, y, 80, 80)
        self.rectangle = rect
        self.pos = new_pos

        return Board,move

    def copy(self):

        rectangle = self.rectangle.copy()
        image = self.image.copy()
        return Pawn(self.pos, self.color, self.coinIndex, rectangle, image)
