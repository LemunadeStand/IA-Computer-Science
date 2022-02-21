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

def displayInit(resX,resY):
    display = []
    #Displays 0-4
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
    settingsButtons.append(Button((247,13,5),(resX-200)/2,(resY-400)/2,250,100,False,"Negatives"))
    #Display timer or not
    settingsButtons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+450,200,100,False,"Timer"))
    #Home Button
    settingsButtons.append(Button((42,191,62),(resX-200)/2,(resY-600)/2+600,200,100,False,"Home"))
    #Clear Leaderboard Button
    settingsButtons.append(Button((42,191,62),300,0,200,100,False,"Clear LB"))
    return settingsButtons

def variablesInit():
    variables = {
        #If a function has been selected: Multiplication, Division, Addition, Subtraction
        'isDoingFunction': False,
        #If the Maximum number has been received yet
        'getMaxNum' : False,
        #If the question has been answered
        'Answered' : False,
        #Include Negative answers for subtraction
        'doNegatives' : False,
        #If settings is being shown
        'showSettings' : False,
        #If 10 questions have been answered
        'showAnswers' : False,
        #Whether timer is shown
        'showTimer' : True,
        #Show leaderboard screen
        'showLeader' : False,
        #Got perfect score or not
        'perfectScore' : True,
        #Leaderboard temporary record string
        'record' : "",
        #The two numbers that are outputted
        'num1' : 0,
        'num2' : 0,
        #Current Position of the top leaderboard page
        'currentPos' : 0,
        #Beginning and End times
        'begin' : 0,
        'end' : 0,
        #Maximum Number
        'MaxNum' : 0,
        #The answer that is calculated by computer
        'answer' : 0,
        #The answer that is entered by the user
        'userAnswer' : 0,
        'currentQuestion' : 0,
        #Letter counter for leaderboard entry
        'counter' : 0
    }
    return variables