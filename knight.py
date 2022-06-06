from selection import Selection
import pygame,copy
from move import Move
class Knight:
    def __init__(self, pos, color, coinindex, rectangle, image):
        self.pos = pos
        self.color = color
        self.coinIndex = coinindex
        self.rectangle = rectangle
        self.image = image
        self.type = "Knight"

    def on_board(self,pos):
        if pos[0] > -1 and pos[1] > -1 and pos[0] < 8 and pos[1] < 8:
            return True

    def find_destinations(self, Board):
        dest = []
        kills = []
        x,y = self.pos
        for i in range(-2,3):
            for j in range(-2,3):
                if i ** 2 + j**2 ==5:
                    pos = [i + x, j + y]
                    if self.on_board(pos):
                        if Board[i+x][j+y] == None:
                            dest.append(Selection([i+x, j+y], False))
                        elif Board[i+x][j+y] != None:
                            if Board[i+x][j+y].color != self.color:
                                dest.append(Selection([i+x, j+y], True))
                                kills.append(Selection([i+x, j+y], True))

        return dest,kills
    def change_pos(self, new_pos, Board, from_obj, kill_obj, kill, check):
        i, j = new_pos
        x = j * 80
        y = i * 80
        Board[i][j] = Board[self.pos[0]][self.pos[1]]
        Board[self.pos[0]][self.pos[1]] = None
        move = Move([self.pos[0], self.pos[1]], new_pos, from_obj, kill_obj, kill, check)
        rect = pygame.Rect(x, y, 80, 80)
        self.rectangle = rect
        self.pos = new_pos

        return Board, move

    def copy(self):
        rectangle = self.rectangle.copy()
        image = self.image.copy()
        return Knight(self.pos, self.color, self.coinIndex, rectangle, image)


