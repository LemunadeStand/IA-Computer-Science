import pygame as pg
from objects.visual.display import Display
class Button(Display):
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.getX() and pos[0] < self.getX() + self.getWidth():
            if pos[1] > self.getY() and pos[1] < self.getY() + self.getHeight():
                return True
            
        return False
    def draw(self,window,outlineColor=None):
        if outlineColor:
            pg.draw.rect(window, outlineColor, (self.getX()-2,self.getY()-2,self.getWidth()+4,self.getHeight()+4),0)
            
        pg.draw.rect(window, self.color, (self.getX(),self.getY(),self.getWidth(),self.getHeight()),0)
        
        if self.getText() != '':
            font = pg.font.SysFont('Arial', 60)
            text = font.render(self.getText(), 1, (0,0,0))
            window.blit(text, (self.getX() + (self.getWidth()/2 - text.get_width()/2), self.getY() + (self.getHeight()/2 - text.get_height()/2)))