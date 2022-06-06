import pygame,copy
from selection import Selection
from move import Move
class Rook:
    def __init__(self, pos, color, coinindex, rectangle, image):
        self.pos = pos
        self.color = color
        self.coinIndex = coinindex
        self.rectangle = rectangle
        self.image = image
        self.type = "Rook"

    def find_destinations(self,Board):
        dest = []
        kills = []
        x,y = self.pos
        # Forward For Black and BackWard For White
        for i in range(x+1,8):
            try:
                if Board[i][y] != None:
                    if Board[i][y].color !=self.color:
                        dest.append(Selection([i, y], True))
                        kills.append(Selection([i, y], True))

                    break
            except:
                pass
            dest.append(Selection([i, y], False))

        # Forward For White and BackWard For Black
        for i in range(x - 1,-1,-1):
            try:
                if Board[i][y] != None:
                    if Board[i][y].color !=self.color:
                        dest.append(Selection([i, y], True))
                        kills.append(Selection([i, y], True))

                    break
            except:
                pass
            dest.append(Selection([i, y], False))

        # Left
        for i in range(y-1,-1,-1):
            try:
                if Board[x][i] != None:
                    if Board[x][i].color != self.color:
                        dest.append(Selection([x, i], True))
                        kills.append(Selection([x, i], True))

                    break
            except:
                pass
            dest.append(Selection([x, i], False))
        # Right
        for i in range(y+1,8):
            try:
                if Board[x][i] != None:
                    if Board[x][i].color !=self.color:
                        dest.append(Selection([x, i], True))
                        kills.append(Selection([x, i], True))

                    break
            except:
                pass
            dest.append(Selection([x, i], False))

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
        return Rook(self.pos, self.color, self.coinIndex, rectangle, image)

