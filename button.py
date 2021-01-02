import pygame as pg

class Button():
    #Initialize Button with optional text
    def __init__(self, color, x,y,width,height,visible, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.visible = visible

    #Draws button with optional outline color
    def drawButton(self,window,outlineColor=None):
        if outlineColor:
            pg.draw.rect(window, outlineColor, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pg.font.SysFont('Arial', 60)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    def setText(self,text):
        self.text=text