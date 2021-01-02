"""
Ideas:
Add ability to change resolution of resX and resY
"""
import pygame as pg
import random
from button import Button
pg.init()
pg.font.init()

resX = 800
resY = 1000
#difference in pixels
dif = int(resX/5)
output = ""
funcType = ""

game_window = pg.display.set_mode((resX, resY))

buttons = []
for x in range(10):
    if x<5:
        tempButton = Button((42,191,62), dif*x,resY-2*dif,dif,dif,False,str(x))
        buttons.append(tempButton)
    else:
        tempButton = Button((42,191,62), dif*(x-5),resY-dif,dif,dif,False,str(x))
        buttons.append(tempButton)
#Operation buttons 10-13
buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2,200,100,True,"Multiply"))
buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+150,200,100,True,"Divide"))
buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+300,200,100,True,"Add"))
buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+450,200,100,True,"Subtract"))
#Display buttons 14-16
buttons.append(Button((0,150,150),(resX-400)/2+300,(resY-400)/2-200,200,100,False))
buttons.append(Button((0,150,150),(resX-400)/2+300,(resY-400)/2-100,200,100,False))
buttons.append(Button((0,0,0),(resX-400)/2+300,(resY-400)/2,200,5,False))
#Max Number buttons last 3
buttons.append(Button((42,191,62),(resX-400)/2,resY/2,300,100,False,"Enter"))
buttons.append(Button((0,150,150),(resX-400)/2,(resY-400)/2,300,100,False,"Max Number: "))
buttons.append(Button((0,150,150),(resX-400)/2+300, (resY-400)/2,200,100,False))

pg.display.set_caption("Math Game")

def update(draw,maxNum):
    game_window.fill((0, 150, 150))
    if draw:
        for x in range(0,10):
            buttons[x].drawButton(game_window,(0,0,0))
            buttons[x].visible = True
        buttons[len(buttons)-1].drawButton(game_window)
        buttons[len(buttons)-3].drawButton(game_window,(0,0,0))
        buttons[len(buttons)-1].visible = True
        buttons[len(buttons)-3].visible = True
        for x in range(10,14):
            buttons[x].visible = False
        if not maxNum:
            buttons[14].visible = True
            buttons[15].visible = True
            buttons[16].visible = True
            buttons[14].drawButton(game_window)
            buttons[15].drawButton(game_window)
            buttons[16].drawButton(game_window)
    else:
        for x in range(10,14):
            buttons[x].drawButton(game_window,(0,0,0))
            buttons[x].visible = True
        for x in range(0,10):
            buttons[x].visible = False
        buttons[len(buttons)-1].visible = False
        buttons[len(buttons)-3].visible = False
    if maxNum:
        buttons[len(buttons)-2].drawButton(game_window)

running = True
isDoingFunction = False
getMaxNum = False
notAnswered = False
doNegatives = True
num1 = 0
num2 = 0
MaxNum = 0
answer = 0
userAnswer = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN: 
            for x in range(len(buttons)):
                if buttons[x].visible:
                    if buttons[x].isOver(pg.mouse.get_pos()):
                        if x<=9:
                            output=output+str(x)
                            buttons[len(buttons)-1].text = output
                        elif x==10:
                            funcType="m"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==11:
                            funcType="d"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==12:
                            funcType="a"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==13:
                            funcType="s"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==len(buttons)-3:
                            notAnswered=True
                            if getMaxNum:
                                MaxNum=int(output)
                                getMaxNum=False
                            else:
                                userAnswer = output
                            output=""
                            buttons[len(buttons)-1].text = output
        elif event.type == pg.MOUSEBUTTONUP: 
            pass
        elif event.type == pg.MOUSEMOTION:
            for x in range(len(buttons)-2):
                if buttons[x].isOver(pg.mouse.get_pos()):
                    buttons[x].color = (42,232,67)
                else:
                    buttons[x].color = (42,191,62)
                buttons[14].color = (0,150,150)
                buttons[15].color = (0,150,150)
                buttons[16].color = (0,0,0)
        if funcType != "":
            if notAnswered:
                if funcType == "m":
                    num1 = random.randint(1,MaxNum)
                    num2 = random.randint(1,MaxNum)
                    answer = num1*num2
                    buttons[14].text = "    "+ str(num1)
                    buttons[15].text = "x   "+(str(num2))
                    notAnswered = False
                elif funcType == "d":
                    num1 = random.randint(1,MaxNum)
                    answer = random.randint(1,MaxNum)
                    num2 = num1*answer
                    buttons[14].text = "    "+ str(num2)
                    buttons[15].text = "÷   "+(str(num1))
                    notAnswered = False
                elif funcType =="a":
                    num1 = random.randint(1,MaxNum)
                    num2 = random.randint(1,MaxNum)
                    answer = num1+num2
                    buttons[14].text = "    "+ str(num1)
                    buttons[15].text = "+   "+(str(num2))
                    notAnswered = False
                elif funcType =="s":
                    if doNegatives:
                        num1 = random.randint(1,MaxNum)
                        num2 = random.randint(1,MaxNum)
                        answer = num1-num2
                    else:
                        num1 = random.randint(1,MaxNum)
                        num2 = random.randint(1,num1)
                        answer = num1-num2
                    buttons[14].text = "    "+ str(num1)
                    buttons[15].text = "-   "+(str(num2))
                    notAnswered = False
    pg.display.update()
    update(isDoingFunction,getMaxNum)