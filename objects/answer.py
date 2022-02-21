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

    def recDiv(self, factor, strNum1, strNum2, counter, answers):
        #End when number being divided is 0 as there are no remainders
        if(int(strNum1)==0):
            return "", answers
        #If the length of the number can't be divided go to next iteration
        if(int(strNum1[0:counter])<int(strNum2)):
            counter=counter+1
            if factor > 1:
                factor = factor/10
            return self.recDiv(factor, strNum1, strNum2, counter, answers)
        else:
            amount = int(int(strNum1[0:counter])/int(strNum2))
            output = "("+strNum2+"x"+str(amount*(int)(factor))+")-"
            strNum1 = str((int)(strNum1)-((int)(strNum2))*(amount*(int)(factor)))
            answers.append(amount*(int)(factor))
            if factor > 1:
                factor = factor/10 #Account for if stays in 1 digits twice
            ttuple = self.recDiv(factor, strNum1, strNum2, 1, answers)
            output = output+ttuple[0]
            return output, ttuple[1]

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
                #Go through digit by digit
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
                #Go through individual digits
                if x <=len(strNum1)-1:
                    temp1 = ((int)(strNum1[len(strNum1)-x-1]))*factor
                if x <=len(strNum2)-1:
                    temp2 = ((int)(strNum2[len(strNum2)-x-1]))*factor
                if self.negative:
                    if x > len(strNum1)-1:
                        if temp2 > 0:
                            #If bottom number is digits longer add negative digits
                            output = output + "(-"+str(temp2) +")+"
                    elif x > len(strNum2)-1:
                        if temp1 > 0:
                            output = output + str(temp1) + "+"
                    else:
                        output = output + str(temp1) + "-" + str(temp2) +"+"
                else:
                    #Carry the one if not large enough
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
                #Work from 1's digit up in strNum2
                temp2 = ((int)(strNum2[len(strNum2)-x-1]))*factor
                for j in range(len(strNum1)):
                    #Work from 1's digit up in strNum1
                    temp1 = ((int)(strNum1[len(strNum1)-j-1]))*tfactor
                    tfactor=tfactor*10
                    if temp1 > 0 and temp2 > 0:
                        #Multiply the individual digits by each other
                        output = output + str(temp2)+"x"+str(temp1)+"+"
                factor = factor*10
                tfactor = 1
            output=output[0:len(output)-1]+"="+str(self.answer)
        elif self.funcType == "÷":
            factor = 10**(len(strNum1)-1)
            answers = []
            output = strNum1+"-"
            #Run recursion to get the output and all answers to steps
            tout, answers = self.recDiv(factor, strNum1, strNum2, 1, answers)
            output = output+tout
            output = output[0:len(output)-1]+"=0||"
            for x in range(len(answers)):
                output = output + str(answers[x])+"+"
            output=output[0:len(output)-1]+"="+str(self.answer)
        return output