import pygame
from selection import Selection
from move import Move
import copy
class Bishop:
    def __init__(self, pos, color, coinindex, rectangle, image,boxColor):
        self.pos = pos
        self.color = color
        self.coinIndex = coinindex
        self.rectangle = rectangle
        self.image = image
        self.boxColor = boxColor
        self.type = "Bishop"
    def find_destinations(self, Board):
        dest = []
        kills =[]
        x,y = self.pos

        # North-East -------------------------------------------
        stepUp = 1
        for i in range(y,8):
            k = x - stepUp
            l = y + stepUp
            if k < 0 or l > 8:
                break
            try:
                if Board[k][l] !=None:
                    if Board[k][l].color != self.color:
                        dest.append(Selection([k, l], True,True))
                        kills.append(Selection([k, l], True,True))

                        break
                    else:
                        break
            except:
                break
            dest.append(Selection([k,l],False,True))
            stepUp += 1


        # North-West -------------------------------------
        stepUp = 1
        for i in range(y, 0, -1):
            k = x - stepUp
            l = y - stepUp
            if k < 0 or l < 0:
                break
            try:
                if Board[k][l] != None:
                    if Board[k][l].color != self.color:
                        dest.append(Selection([k, l], True, True))
                        kills.append(Selection([k, l], True, True))

                        break
                    else:
                        break
            except:
                break
            dest.append(Selection([k, l], False, True))
            stepUp += 1


        # South-West -----------------------------------

        stepUp = 1
        for i in range(y, 0,-1):
            k = x + stepUp
            l = y - stepUp
            if k > 7 or l < 0:
                break
            try:
                if Board[k][l] != None:
                    if Board[k][l].color != self.color:
                        dest.append(Selection([k, l], True, True))
                        kills.append(Selection([k, l], True, True))

                        break
                    else:
                        break
            except:
                break
            dest.append(Selection([k, l], False, True))
            stepUp += 1

        # South-East
        stepUp = 1
        for i in range(y, 8):
            k = x + stepUp
            l = y + stepUp
            if k > 7 or l > 7:
                break
            try:
                if Board[k][l] != None:
                    if Board[k][l].color !=self.color:
                        dest.append(Selection([k, l], True,True))
                        kills.append(Selection([k, l], True,True))

                        break
                    else:
                        break
            except:
                break
            dest.append(Selection([k, l], False,True))
            stepUp += 1

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
        return Bishop(self.pos, self.color, self.coinIndex, rectangle, image,self.boxColor)


