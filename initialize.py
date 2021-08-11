from collections import deque
from objects.linked import Linked
from objects.files import Files
from objects.answer import Answer
from objects.visual.button import Button
from objects.visual.display import Display

def buttonInit(resX,resY):
    buttons = []
    dif = int(resX/5)
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
    #Negative Sign Button 14
    buttons.append(Button((42,191,62),302,resY-2*dif-102,100,100,False,"-"))
    #Delete Button 15
    buttons.append(Button((42,191,62),resX-102,resY-2*dif-102,100,100,False,"Del"))
    #Leaderboard left and right buttons 16 17
    buttons.append(Button((42,191,62),(resX-100),(resY-100),100,100,False,"->"))
    buttons.append(Button((42,191,62),(resX-200),(resY-100),100,100,False,"<-"))
    #Enter Leaderboard Letters Buttons 18 19
    buttons.append(Button((42,191,62),300,resY-100,100,100,False,"↑"))
    buttons.append(Button((42,191,62),500,resY-100,100,100,False,"↓"))
    #Enter Button Last button
    buttons.append(Button((42,191,62),0,resY-2*dif-102,300,100,False,"Enter"))
    return buttons

def answerButtonInit():
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
    return answerButtons

def displayInit(resX,resY,hasInit):
    display = []
    tempDisplay = []
    dif = int(resX/5)
    if hasInit:
        tempDisplay.append(display[0])
        tempDisplay.append(display[1])
        for x in range(5):
            tempDisplay.append(display[x+9])
    
    #Displays 0-4
    if hasInit:
        #Maintain Text within the two numbers displayed
        display.append(tempDisplay[0])
        display[0].setX((resX-400)/2+200)
        display[0].setY((resY-400)/2-200)
        display.append(tempDisplay[1])
        display[1].setX((resX-400)/2+200)
        display[1].setY((resY-400)/2-100)
    else:
        display.append(Display((0,150,150),(resX-400)/2+200,(resY-400)/2-200,200,100,False))
        display.append(Display((0,150,150),(resX-400)/2+200,(resY-400)/2-100,200,100,False))
    display.append(Display((0,0,0),(resX-400)/2+200,(resY-400)/2,200,5,False))
    display.append(Display((0,150,150),(resX-400)/2+200,(resY-400)/2+100,200,100,False))
    display.append(Display((0,150,150),0,(resY-400)/2+200,resX,100,False))
    #Timer Display 5
    display.append(Display((0,150,150),resX-200,0,200,100,False,"0.00"))
    #Number display 6
    display.append(Display((0,150,150),(resX-400)/2+200, (resY-400)/2,200,100,False))
    #Max Num Display text 7
    display.append(Display((0,150,150),(resX-400)/2-100,(resY-400)/2,300,100,False,"Max Number: "))
    #Leaderboard display buttons 8-13
    display.append(Display((0,150,150),300,0,300,100,False,"Leaderboard"))
    if hasInit:
        for x in range(5):
            display.append(tempDisplay[x+2])
    else:
        display.append(Display((0,150,150),200,100,300,100,False))
        display.append(Display((0,150,150),200,200,300,100,False))
        display.append(Display((0,150,150),200,300,300,100,False))
        display.append(Display((0,150,150),200,400,300,100,False))
        display.append(Display((0,150,150),200,500,300,100,False))
    #Leaderboard entry letter display 14
    display.append(Display((0,150,150),400,resY-100,100,100,False,"A"))
    return display

def settingsButtonInit(resX,resY):
    settingsButtons = []
    #General Settings button
    settingsButtons.append(Button((42,191,62),0,0,300,100,True,"Settings"))
    #Negative number button
    settingsButtons.append(Button((247,13,5),(resX-200)/2,(resY-600)/2,250,100,False,"Negatives"))
    #Change screen size
    settingsButtons.append(Button((42,191,62),(resX-500)/2,(resY-600)/2+150,500,100,False,"Change Screen Size"))
    settingsButtons.append(Button((42,191,62),50,(resY-600)/2+300,200,100,False,"800x800"))
    settingsButtons.append(Button((42,191,62),300,(resY-600)/2+300,200,100,False,"800x1000"))
    settingsButtons.append(Button((42,191,62),550,(resY-600)/2+300,200,100,False,"1000x800"))
    #Display timer or not
    settingsButtons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+450,200,100,False,"Timer"))
    #Home Button
    settingsButtons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+600,200,100,False,"Home"))
    #Clear Leaderboard Button
    settingsButtons.append(Button((42,191,62),300,0,200,100,False,"Clear LB"))
    return settingsButtons
