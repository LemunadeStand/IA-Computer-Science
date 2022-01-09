import pygame as pg
import random
import time
from collections import deque
from objects.linked import Linked
from objects.files import Files
from objects.answer import Answer
from objects.visual.button import Button
from objects.visual.display import Display
from initialize import *
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

#Create Current Leaderboard and Load Files
leaderMasterNames = Linked()
leaderMasterScores = Linked()
fileMaster = Files(Files.createScores(), Files.createNames())

#Initialize All buttons/displays
def initialize():
    buttons = buttonInit(resX, resY)
    answerButtons = answerButtonInit()
    display = displayInit(resX, resY)
    settingsButtons = settingsButtonInit(resX, resY)
    variables = variablesInit()
    return buttons, answerButtons, display, settingsButtons, variables
buttons, answerButtons, display, settingsButtons, vars = initialize()

pg.display.set_caption("Math Game")

#Updates drawing of buttons
#Visible just determines if they can be clicked or not; not if they are actually visible
def update(vars,negative):
    game_window.fill((0, 150, 150))
    for x in range(len(settingsButtons)):
        settingsButtons[x].setVisible(False)
    for x in range(len(buttons)):
        buttons[x].setVisible(False)
    for x in range(10):
        answerButtons[x][0].setVisible(False)
    settingsButtons[0].draw(game_window,(0,0,0))
    settingsButtons[0].setVisible(True)
    if vars['showSettings']:
        for x in range(len(settingsButtons)):
            settingsButtons[x].draw(game_window,(0,0,0))
            settingsButtons[x].setVisible(True)
                
    else:
        if vars['isDoingFunction']:
            if vars['showTimer']:
                display[5].setVisible(True)
                display[5].draw(game_window)
            if vars['showAnswers']:
                buttons[len(buttons)-1].setText("Done")
                buttons[len(buttons)-1].setX(0)
                buttons[len(buttons)-1].setY(resY-100)
                buttons[len(buttons)-1].draw(game_window,(0,0,0))
                buttons[len(buttons)-1].setVisible(True)
                if not vars['showLeader']:
                    display[4].setVisible(True)
                    display[4].draw(game_window)
                if vars['showLeader']:
                    for x in range(6):
                        display[x+8].draw(game_window)
                        display[x+8].setVisible(True)
                    buttons[16].setVisible(True)
                    buttons[17].setVisible(True)
                    buttons[16].draw(game_window, (0,0,0))
                    buttons[17].draw(game_window, (0,0,0))
                    if vars['perfectScore']:
                        display[14].draw(game_window)
                        display[14].setVisible(True)
                        buttons[18].setVisible(True)
                        buttons[19].setVisible(True)
                        buttons[18].draw(game_window, (0,0,0))
                        buttons[19].draw(game_window, (0,0,0))
            else:
                for x in range(10):
                    buttons[x].draw(game_window,(0,0,0))
                    buttons[x].setVisible(True)
                buttons[len(buttons)-1].draw(game_window,(0,0,0))
                buttons[len(buttons)-1].setVisible(True)
                buttons[15].draw(game_window,(0,0,0))
                buttons[15].setVisible(True)
                if negative:
                    buttons[14].draw(game_window,(0,0,0))
                    buttons[14].setVisible(True)
            if not vars['showLeader']:
                display[6].draw(game_window)
                display[6].setVisible(True)
            if not vars['getMaxNum'] and not vars['showLeader']:
                for x in range(4):
                    display[x].setVisible(True)
                    display[x].draw(game_window)
                for x in range(10):
                    answerButtons[x][0].draw(game_window,(0,0,0))
                    answerButtons[x][0].setVisible(True)

        else:
            for x in range(10,14):
                buttons[x].draw(game_window,(0,0,0))
                buttons[x].setVisible(True)
        if vars['getMaxNum']:
            display[7].draw(game_window)
            display[7].setVisible(True)

#Begin Game
running = True
while running:
    if vars['end']==0 and vars['isDoingFunction'] and not vars['getMaxNum']:
        display[5].setText("{:.2f}".format(time.time()-vars['begin']))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fileMaster.save()
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN: 
            for x in range(len(buttons)):
                if buttons[x].getVisible():
                    if buttons[x].isOver(pg.mouse.get_pos()):
                        if x<=9:
                            output=output+str(x)
                            display[6].setText(output)
                        elif x==10:
                            funcType="x"
                            vars['isDoingFunction'] = True
                            vars['getMaxNum'] = True
                        elif x==11:
                            funcType="÷"
                            vars['isDoingFunction'] = True
                            vars['getMaxNum'] = True
                        elif x==12:
                            funcType="+"
                            vars['isDoingFunction'] = True
                            vars['getMaxNum'] = True
                        elif x==13:
                            funcType="-"
                            vars['isDoingFunction'] = True
                            vars['getMaxNum'] = True
                        elif x==14 and not vars['getMaxNum']:
                            output = output +"-"
                            display[6].setText(output)
                        elif x==15 and len(output)>0:
                            output = output[0:len(output)-1]
                            display[6].setText(output)
                        elif x==16:
                            if(vars['currentPos']+5<leaderMasterScores.size):
                                vars['currentPos']+=5
                                if(leaderMasterScores.size>=vars['currentPos']+5):
                                    for x in range(5):
                                        display[x+9].setText(leaderMasterNames[vars['currentPos']+x]+" "+str(leaderMasterScores[vars['currentPos']+x]))
                                else:
                                    tempnum = 0
                                    for x in range(leaderMasterScores.size-vars['currentPos']):
                                        display[x+9].setText(leaderMasterNames[vars['currentPos']+x]+" "+str(leaderMasterScores[vars['currentPos']+x]))
                                        tempnum+=1
                                    for x in range(vars['currentPos']+5-leaderMasterScores.size):
                                        display[x+9+tempnum].setText("--- --.--")
                        elif x==17:
                            if(vars['currentPos']-5>=0):
                                vars['currentPos']-=5
                                for x in range(5):
                                    display[x+9].setText(leaderMasterNames[vars['currentPos']+x]+" "+str(leaderMasterScores[vars['currentPos']+x]))
                        elif x==18:
                            if(display[14].getText()=="Z"):
                                display[14].setText("A")
                            else:
                                display[14].setText(chr(ord(display[14].getText())+1))
                        elif x==19:
                            if(display[14].getText()=="A"):
                                display[14].setText("Z")
                            else:
                                display[14].setText(chr(ord(display[14].getText())-1))
                        elif x==len(buttons)-1:
                            if vars['getMaxNum']:
                                if output != "":
                                    vars['MaxNum']=int(output)
                                    vars['Answered']=True
                                    vars['getMaxNum'] = False
                                    vars['begin'] = time.time()
                                    leaderMasterNames = fileMaster.getMasterNames(funcType)
                                    leaderMasterScores = fileMaster.getMasterScores(funcType)
                            elif vars['currentQuestion']<=9 and not vars['showLeader']:
                                if output =="":
                                    output = "0"
                                vars['userAnswer'] = int(output)
                                vars['Answered']=True
                                #Adds answers to array of answer buttons
                                answerButtons[vars['currentQuestion']].append(Answer(vars['num1'],vars['num2'],vars['answer'],vars['userAnswer'], vars['userAnswer']==vars['answer'],funcType,vars['doNegatives']))
                                #Checks if users answer is correct
                                if vars['userAnswer'] == vars['answer']:
                                    answerButtons[vars['currentQuestion']][0].color = (17,247,5)
                                else:
                                    answerButtons[vars['currentQuestion']][0].color = (247,13,5)
                                    vars['perfectScore'] = False
                                #Recognize when 10 questions have been answered
                                if vars['currentQuestion'] < 9:
                                    vars['currentQuestion'] = vars['currentQuestion'] + 1
                                else:
                                    vars['showAnswers'] = True
                                    vars['currentQuestion']=vars['currentQuestion']+1
                                    display[3].setText("Your Answer: " + str(answerButtons[9][1].userAnswer))
                                    display[0].setText("    "+str(answerButtons[9][1].num1))
                                    display[1].setText(funcType+"   "+str(answerButtons[9][1].num2))
                                    vars['Answered'] = False
                                    vars['end'] = time.time()
                            #Go to leaderboard screen
                            elif vars['currentQuestion'] > 9 and vars['showAnswers']:
                                vars['currentQuestion'] = 0
                                vars['showLeader'] = True
                                if(leaderMasterScores.size>=5):
                                    for x in range(5):
                                        display[x+9].setText(leaderMasterNames[vars['currentPos']+x]+" "+str(leaderMasterScores[vars['currentPos']+x]))
                                else:
                                    for x in range(leaderMasterScores.size):
                                        display[x+9].setText(leaderMasterNames[vars['currentPos']+x]+" "+str(leaderMasterScores[vars['currentPos']+x]))
                                    for x in range(5-leaderMasterScores.size):
                                        display[x+9+leaderMasterScores.size].setText("--- --.--")
                            #Reset for another time around
                            elif vars['showLeader'] and vars['showAnswers']:
                                #3 letters for initials in leaderboard
                                if vars['perfectScore'] and vars['counter']<3:
                                    vars['counter']+=1
                                    vars['record']+=display[14].getText()
                                else:
                                    if(vars['counter']==3):
                                        fileMaster.add(funcType, round(vars['end']-vars['begin'],2), vars['record'])
                                    buttons, answerButtons, display, settingsButtons, vars = initialize()
                            output=""
                            display[6].setText(output)
                            if vars['showAnswers']:
                                display[6].setText("Correct Answer: " + str(answerButtons[9][1].answer))
            for x in range(len(settingsButtons)):
                if settingsButtons[x].getVisible():
                    if settingsButtons[x].isOver(pg.mouse.get_pos()):
                        if x==0:
                            vars['showSettings'] = not vars['showSettings']
                        elif x==1:
                            if vars['doNegatives']:
                                settingsButtons[x].color = (247,13,5)
                            else:
                                settingsButtons[x].color = (42,191,62)
                            vars['doNegatives'] = not vars['doNegatives']
                        elif x==2:
                            if vars['showTimer']:
                                settingsButtons[x].color = (247,13,5)
                            else:
                                settingsButtons[x].color = (42,191,62)
                            vars['showTimer'] = not vars['showTimer']
                        elif x==3:
                            buttons, answerButtons, display, settingsButtons, vars = initialize()
                        elif x==4:
                            fileMaster.clear()
            if vars['showAnswers']:
                for x in range(10):
                    if answerButtons[x][0].isOver(pg.mouse.get_pos()):
                        display[6].setText("Correct Answer: " + str(answerButtons[x][1].answer))
                        display[3].setText("Your Answer: " + str(answerButtons[x][1].userAnswer))
                        display[0].setText("    "+str(answerButtons[x][1].num1))
                        display[1].setText(funcType+"   "+str(answerButtons[x][1].num2))
                        display[4].setText(answerButtons[x][1].getExplanation())
                        
        elif event.type == pg.MOUSEMOTION:
            for x in range(len(buttons)):
                if buttons[x].isOver(pg.mouse.get_pos()):
                    buttons[x].color = (42,232,67)
                else:
                    buttons[x].color = (42,191,62)
            if vars['showAnswers']:
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
            if vars['Answered']:
                if funcType == "x":
                    vars['num1'] = random.randint(1,vars['MaxNum'])
                    vars['num2'] = random.randint(1,vars['MaxNum'])
                    vars['answer'] = vars['num1']*vars['num2']
                elif funcType == "÷":
                    vars['num2'] = random.randint(1,vars['MaxNum'])
                    vars['answer'] = random.randint(1,vars['MaxNum'])
                    vars['num1'] = vars['num2']*vars['answer']
                elif funcType =="+":
                    vars['num1'] = random.randint(1,vars['MaxNum'])
                    vars['num2'] = random.randint(1,vars['MaxNum'])
                    vars['answer'] = vars['num1']+vars['num2']
                elif funcType =="-":
                    if vars['doNegatives']:
                        vars['num1'] = random.randint(1,vars['MaxNum'])
                        vars['num2'] = random.randint(1,vars['MaxNum'])
                        vars['answer'] = vars['num1']-vars['num2']
                    else:
                        vars['num1'] = random.randint(1,vars['MaxNum'])
                        vars['num2'] = random.randint(1,vars['num1'])
                        vars['answer'] = vars['num1']-vars['num2']
                display[0].setText("    "+ str(vars['num1']))
                display[1].setText(funcType+"   "+(str(vars['num2'])))
                vars['Answered'] = False
    pg.display.update()
    update(vars,vars['doNegatives'] and len(output)==0)