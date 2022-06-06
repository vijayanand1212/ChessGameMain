import pygame
class Selection:
    def __init__(self,pos,kill=False,slant=False):
        self.pos = pos
        xpos = pos[1] * 80
        ypos = pos[0] * 80
        rect = pygame.Rect(xpos + 5, ypos + 5, 70, 70)
        self.rectangle = rect
        self.kill = kill
        self.slant = slant
