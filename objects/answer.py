import pygame as pg
class Answer():
    #Initialize variables needed to display answers
    def __init__(self, num1, num2, answer, userAnswer, correct, funcType, negative):
        self.num1 = num1
        self.num2 = num2
        self.answer = answer
        self.userAnswer = userAnswer
        self.correct = correct
        self.funcType = funcType
        self.negative = negative
    #Make explanation
    def getExplanation(self):
        output = ""
        strNum1 = str(self.num1)
        strNum2 = str(self.num2)
        maxLength = len(strNum1)
        factor = 1
        if(len(strNum2)>maxLength):
            maxLength = len(strNum2)
        if self.funcType == "+":
            for x in range(maxLength):
                if x<=len(strNum1)-1:
                    temp1 = str(((int)(strNum1[len(strNum1)-x-1]))*factor)
                if x<=len(strNum2)-1:
                    temp2 = str(((int)(strNum2[len(strNum2)-x-1]))*factor)
                if x > len(strNum1)-1:
                    output = output + temp2 +"+"
                elif x > len(strNum2)-1:
                    output = output + temp1 + "+"
                else:
                    output = output + temp1 + "+" + temp2 +"+"
                factor=factor*10
            output=output[0:len(output)-1]+"="+str(self.answer)
        elif self.funcType =="-":
            diff = 0
            for x in range(maxLength):
                if x <=len(strNum1)-1:
                    temp1 = ((int)(strNum1[len(strNum1)-x-1]))*factor
                if x <=len(strNum2)-1:
                    temp2 = ((int)(strNum2[len(strNum2)-x-1]))*factor
                if self.negative:
                    if x > len(strNum1)-1:
                        if temp2 > 0:
                            output = output + "(-"+str(temp2) +")"+"+"
                    elif x > len(strNum2)-1:
                        if temp1 > 0:
                            output = output + str(temp1) + "+"
                    else:
                        output = output + str(temp1) + "-" + str(temp2) +"+"
                else:
                    temp1 = temp1-diff*factor
                    diff=0
                    if temp1<temp2 and x <= len(strNum2)-1:
                        diff=1
                        temp1=temp1+factor*10
                    if x > len(strNum2)-1:
                        output = output + str(temp1) + "+"
                    else:
                        output = output + str(temp1)+"-"+str(temp2)+"+"
                factor=factor*10
            output=output[0:len(output)-1]+"="+str(self.answer)
        elif self.funcType == "x":
            tfactor = factor
            for x in range(len(strNum2)):
                temp2 = ((int)(strNum2[len(strNum2)-x-1]))*factor
                for j in range(len(strNum1)):
                    temp1 = ((int)(strNum1[len(strNum1)-j-1]))*tfactor
                    tfactor=tfactor*10
                    if temp1 > 0 and temp2 > 0:
                        output = output + str(temp2)+"x"+str(temp1)+"+"
                factor = factor*10
                tfactor = 1
            output=output[0:len(output)-1]+"="+str(self.answer)
        elif self.funcType == "÷":
            factor = 10**(len(strNum1)-1)
            done = False
            counter = 1
            answers = []
            output = strNum1+"-"
            while int(strNum1) > 0:
                done = False
                while not done:
                    temp1=strNum1[0:counter]
                    if int(temp1)<int(strNum2):
                        counter=counter+1
                    else:
                        amount = int(int(temp1)/int(strNum2))
                        output = output+"("+strNum2+"x"+str(amount*(int)(factor))+")-"
                        strNum1 = str((int)(strNum1)-((int)(strNum2))*(amount*(int)(factor)))
                        answers.append(amount*(int)(factor))
                        done = True
                    if factor > 1:
                        factor = factor/10
            output = output[0:len(output)-1]+"=0||"
            for x in range(len(answers)):
                output = output + str(answers[x])+"+"
            output=output[0:len(output)-1]+"="+str(self.answer)
        return output