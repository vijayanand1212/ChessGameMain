from bishop import Bishop
from selection import Selection
from rook import Rook
from move import Move
import pygame

class Queen():
    def __init__(self, pos, color, coinindex, rectangle, image):
        self.pos = pos
        self.color = color
        self.coinIndex = coinindex
        self.rectangle = rectangle
        self.image = image
        self.type = "Queen"

    def find_destinations(self,Board):
        dest = []
        kills = []
        x,y = self.pos
        slant,killsBishop = Bishop.find_destinations(self,Board)
        rook,killsrook = Rook.find_destinations(self,Board)

        dest += slant
        dest += rook
        kills = killsBishop + killsrook
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
        return Queen(self.pos, self.color, self.coinIndex, rectangle, image)
