import pygame as pg

class Display():
    def __init__(self, color, x,y,width,height,visible, text=''):
        self.color = color
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__visible = visible

    def draw(self,window):    
        pg.draw.rect(window, self.color, (self.__x,self.__y,self.__width,self.__height),0)
        if self.__text != '':
            font = pg.font.SysFont('Arial', 60)
            text = font.render(self.__text, 1, (0,0,0))
            #Divide by 2 for width and height to center text
            window.blit(text, (self.__x + (self.__width/2 - text.get_width()/2),
                               self.__y + (self.__height/2 - text.get_height()/2)))
    def setText(self,text):
        self.__text=text
    def getText(self):
        return self.__text
    def setWidth(self, width):
        self.__width = width
    def getWidth(self):
        return self.__width
    def setHeight(self, height):
        self.__height=height
    def getHeight(self):
        return self.__height
    def setX(self, x):
        self.__x=x
    def getX(self):
        return self.__x
    def setY(self, y):
        self.__y=y
    def getY(self):
        return self.__y
    def setVisible(self, visible):
        self.__visible=visible
    def getVisible(self):
        return self.__visible
