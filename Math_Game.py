"""
Ideas:
At pc at home
"""
import pygame as pg
import random
from button import Button
from answer import Answer
pg.init()
pg.font.init()

#Resolution
resX = 800
resY = 800
#Difference in pixels
dif = int(resX/5)
output = ""
funcType = ""

#Creating window based onn resolution
game_window = pg.display.set_mode((resX, resY))

buttons = []
answerButtons = [[]]
#Creating the answer buttons for explanations
for x in range(10):
    if x<5:
        tempArray = []
        answerButtons.append(tempArray)
        answerButtons[x].append(Button((0,150,150),50*x,100,50,50,False))
    else:
        tempArray = []
        answerButtons.append(tempArray)
        answerButtons[x].append(Button((0,150,150),50*(x-5),150,50,50,False))
pg.display.set_caption("Math Game")
settingsButtons = []
tempButtons = []

def initialize(hasInit):
    dif = int(resX/5)
    tempButtons.clear()
    if hasInit:
        tempButtons.append(buttons[14])
        tempButtons.append(buttons[15])
    buttons.clear()
    settingsButtons.clear()
    #Buttons of 0-9
    for x in range(10):
        if x<5:
            buttons.append(Button((42,191,62), dif*x,resY-2*dif,dif,dif,False,str(x)))
        else:
            buttons.append(Button((42,191,62), dif*(x-5),resY-dif,dif,dif,False,str(x)))
    #Operation buttons 10-13
    buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2,200,100,True,"Multiply"))
    buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+150,200,100,True,"Divide"))
    buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+300,200,100,True,"Add"))
    buttons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+450,200,100,True,"Subtract"))
    #Display buttons 14-18
    if hasInit:
        buttons.append(tempButtons[0])
        buttons[14].x=(resX-400)/2+200
        buttons[14].y=(resY-400)/2-200
        buttons.append(tempButtons[1])
        buttons[15].x=(resX-400)/2+200
        buttons[15].y=(resY-400)/2-100
    else:
        buttons.append(Button((0,150,150),(resX-400)/2+200,(resY-400)/2-200,200,100,False))
        buttons.append(Button((0,150,150),(resX-400)/2+200,(resY-400)/2-100,200,100,False))
    buttons.append(Button((0,0,0),(resX-400)/2+200,(resY-400)/2,200,5,False))
    buttons.append(Button((0,150,150),(resX-400)/2+200,(resY-400)/2+100,200,100,False))
    buttons.append(Button((0,150,150),0,(resY-400)/2+200,resX,100,False))
    #Max Number buttons last 3
    buttons.append(Button((42,191,62),0,resY-2*dif-102,300,100,False,"Enter"))
    buttons.append(Button((0,150,150),(resX-400)/2-100,(resY-400)/2,300,100,False,"Max Number: "))
    buttons.append(Button((0,150,150),(resX-400)/2+200, (resY-400)/2,200,100,False))

    #General Settings button
    settingsButtons.append(Button((42,191,62),0,0,300,100,True,"Settings"))
    #Negative number button
    settingsButtons.append(Button((247,13,5),(resX-200)/2,(resY-600)/2,250,100,False,"Negatives"))
    #Change screen size
    settingsButtons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+150,300,100,False,"Change Screen Size"))
    settingsButtons.append(Button((42,191,62),50,(resY-600)/2+300,200,100,False,"800x800"))
    settingsButtons.append(Button((42,191,62),300,(resY-600)/2+300,200,100,False,"800x1000"))
    settingsButtons.append(Button((42,191,62),550,(resY-600)/2+300,200,100,False,"1000x800"))

#Updates drawing of buttons
#Visible just determines if they can be clicked or not; not if they are actually visible
def update(draw,maxNum,settings,screen,review):
    game_window.fill((0, 150, 150))
    for x in range(len(settingsButtons)):
        settingsButtons[x].visible = False
    for x in range(len(buttons)):
        buttons[x].visible = False
    for x in range(10):
        answerButtons[x][0].visible = False
    settingsButtons[0].drawButton(game_window,(0,0,0))
    settingsButtons[0].visible = True
    if settings:
        for x in range(len(settingsButtons)):
            if x<3:
                settingsButtons[x].drawButton(game_window,(0,0,0))
                settingsButtons[x].visible = True
            elif screen:
                settingsButtons[x].drawButton(game_window, (0,0,0))
                settingsButtons[x].visible = True
                

    else:
        if draw:
            if review:
                buttons[len(buttons)-3].text = "Done"
                buttons[len(buttons)-3].x = 0
                buttons[len(buttons)-3].y = resY-100
                buttons[len(buttons)-3].drawButton(game_window,(0,0,0))
                buttons[len(buttons)-3].visible = True
                buttons[18].visible = True
                buttons[18].drawButton(game_window)
            else:
                for x in range(10):
                    buttons[x].drawButton(game_window,(0,0,0))
                    buttons[x].visible = True
                buttons[len(buttons)-3].drawButton(game_window,(0,0,0))
                buttons[len(buttons)-3].visible = True
            buttons[len(buttons)-1].drawButton(game_window)
            buttons[len(buttons)-1].visible = True
            if not maxNum:
                buttons[14].visible = True
                buttons[15].visible = True
                buttons[16].visible = True
                buttons[17].visible = True
                buttons[14].drawButton(game_window)
                buttons[15].drawButton(game_window)
                buttons[16].drawButton(game_window)
                buttons[17].drawButton(game_window)
                for x in range(10):
                    answerButtons[x][0].drawButton(game_window,(0,0,0))
                    answerButtons[x][0].visible = True

        else:
            for x in range(10,14):
                buttons[x].drawButton(game_window,(0,0,0))
                buttons[x].visible = True
        if maxNum:
            buttons[len(buttons)-2].drawButton(game_window)
            buttons[len(buttons)-2].visible = True

running = True
#If a function has been selected: Multiplication, Division, Addition, Subtraction
isDoingFunction = False
#If the Maximum number has been received yet
getMaxNum = False
#If the question has been answered
Answered = False
#Include Negative answers for subtraction
doNegatives = False
#If settings is being shown
showSettings = False
#Determines if screen is being changed
changeScreen = False
#If 10 questions have been answered
showAnswers = False
#The two numbers that are outputted
num1 = 0
num2 = 0
#Maximum Number
MaxNum = 0
#The answer that is calculated by computer
answer = 0
#The answer that is entered by the user
userAnswer = 0
currentQuestion = 0
counter = 0
firstInit = False
initialize(firstInit)
firstInit = True
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
                            funcType="x"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==11:
                            funcType="÷"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==12:
                            funcType="+"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==13:
                            funcType="-"
                            isDoingFunction = True
                            getMaxNum = True
                        elif x==len(buttons)-3:
                            if getMaxNum:
                                if output != "":
                                    MaxNum=int(output)
                                    Answered=True
                                    getMaxNum = False
                            elif currentQuestion<=9:
                                if output =="":
                                    output = "0"
                                userAnswer = int(output)
                                Answered=True
                                #Adds answers to array of answer buttons
                                answerButtons[currentQuestion].append(Answer(num1,num2,answer,userAnswer, userAnswer==answer,funcType,doNegatives))
                                #Checks if users answer is correct
                                if userAnswer == answer:
                                    answerButtons[currentQuestion][0].color = (17,247,5)
                                else:
                                    answerButtons[currentQuestion][0].color = (247,13,5)
                                #Recognize when 10 questions have been answered
                                if currentQuestion < 9:
                                    currentQuestion = currentQuestion + 1
                                else:
                                    showAnswers = True
                                    currentQuestion=currentQuestion+1
                                    buttons[17].text = "Your Answer: " + str(answerButtons[9][1].userAnswer)
                                    buttons[14].text = "    "+str(answerButtons[9][1].num1)
                                    buttons[15].text = funcType+"   "+str(answerButtons[9][1].num2)
                                    Answered = False
                            #Reset for another time around
                            elif currentQuestion > 9 and showAnswers:
                                isDoingFunction = False
                                showAnswers = False
                                buttons[len(buttons)-3].text = "Enter"
                                buttons[len(buttons)-3].x = 0
                                buttons[len(buttons)-3].y = resY-2*dif-102
                                currentQuestion = 0
                                for x in range(10):
                                    answerButtons[x].pop(1)
                                    answerButtons[x][0].color = (0,150,150)
                                buttons[17].text = ""
                            output=""
                            buttons[len(buttons)-1].text = output
                            if showAnswers:
                                buttons[len(buttons)-1].text = "Correct Answer: " + str(answerButtons[9][1].answer)
            for x in range(len(settingsButtons)):
                if settingsButtons[x].visible:
                    if settingsButtons[x].isOver(pg.mouse.get_pos()):
                        if x==0:
                            showSettings = not showSettings
                        elif x==1:
                            if doNegatives:
                                settingsButtons[x].color = (247,13,5)
                            else:
                                settingsButtons[x].color = (42,191,62)
                            doNegatives = not doNegatives
                        elif x==2:
                            changeScreen = not changeScreen
                        elif x==3 or x==4 or x==5:
                            resX = (int)(settingsButtons[x].text[0:settingsButtons[x].text.find("x")])
                            resY = (int)(settingsButtons[x].text[settingsButtons[x].text.find("x")+1:len(settingsButtons[x].text)])
                            game_window = pg.display.set_mode((resX,resY))
                            initialize(firstInit)
            if showAnswers:
                for x in range(10):
                    if answerButtons[x][0].isOver(pg.mouse.get_pos()):
                        buttons[len(buttons)-1].text = "Correct Answer: " + str(answerButtons[x][1].answer)
                        buttons[17].text = "Your Answer: " + str(answerButtons[x][1].userAnswer)
                        buttons[14].text = "    "+str(answerButtons[x][1].num1)
                        buttons[15].text = funcType+"   "+str(answerButtons[x][1].num2)
                        buttons[18].text=answerButtons[x][1].getExplanation()
                        
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
                buttons[17].color = (0,150,150)
                buttons[18].color = (0,150,150)
            if showAnswers:
                for x in range(10):
                    if answerButtons[x][0].isOver(pg.mouse.get_pos()):
                        if not answerButtons[x][1].correct:
                            answerButtons[x][0].color = (209, 17, 10)
                        else:
                            answerButtons[x][0].color = (42,232,67)
                    else:
                        if not answerButtons[x][1].correct:
                            answerButtons[x][0].color = (247, 13, 5)
                        else:
                            answerButtons[x][0].color = (17,247,5)
        if funcType != "":
            if Answered:
                if funcType == "x":
                    num1 = random.randint(1,MaxNum)
                    num2 = random.randint(1,MaxNum)
                    answer = num1*num2
                    buttons[14].text = "    "+ str(num1)
                    buttons[15].text = "x   "+(str(num2))
                    Answered = False
                elif funcType == "÷":
                    num2 = random.randint(1,MaxNum)
                    answer = random.randint(1,MaxNum)
                    num1 = num2*answer
                    buttons[14].text = "    "+ str(num1)
                    buttons[15].text = "÷   "+(str(num2))
                    Answered = False
                elif funcType =="+":
                    num1 = random.randint(1,MaxNum)
                    num2 = random.randint(1,MaxNum)
                    answer = num1+num2
                    buttons[14].text = "    "+ str(num1)
                    buttons[15].text = "+   "+(str(num2))
                    Answered = False
                elif funcType =="-":
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
                    Answered = False
    pg.display.update()
    update(isDoingFunction,getMaxNum,showSettings,changeScreen,showAnswers)