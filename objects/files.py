from objects.linked import Linked
import os
class Files():
    #XS is "X" function scores and XN is "X" function name
    def __init__(self, scores, names):
        self.scores = Linked([scores[0], scores[1], scores[2], scores[3]])
        self.names = Linked([names[0], names[1], names[2], names[3]])
    
    def clear(self):
        for x in self.scores:
            x.clearq()
        for x in self.names:
            x.clearq()
        realdir=os.getcwd()
        #Go thru scores and clear files
        os.chdir(os.getcwd()+"/leaderboard/scores")
        for file in os.listdir():
            f = open(file, "w")
            f.write("")
            f.close()
        #Go thru names and clear files
        os.chdir(realdir+"/leaderboard/names")
        for file in os.listdir():
            f = open(file, "w")
            f.write("")
            f.close()
        #Resyn current working directory
        os.chdir(realdir)

    def save(self):
        realdir=os.getcwd()
        os.chdir(os.getcwd()+"/leaderboard/scores")
        i = 0
        for file in os.listdir():
            f = open(file, "w")
            for x in self.scores[i]:
                f.write(x+"\n")
            f.close()
            i+=1
        i = 0
        os.chdir(realdir+"/leaderboard/names")
        for file in os.listdir():
            f = open(file, "w")
            for x in self.names[i]:
                f.write(x)
            f.close()
            i+=1
    
    def add(self, funcType, score, name):
        x=0
        i=0
        if funcType=="+":
            i=0
        elif funcType=="-":
            i=3
        elif funcType=="x":
            i=2
        elif funcType=="÷":
            i=1
        while x<self.scores[i].size and score>float(self.scores[i][x]):
            x+=1
        if x==self.scores[i].size:
            self.scores[i].insertTail(str(score))
            self.names[i].insertTail(name)
        else:
            self.scores[i].insertBefore(x, str(score))
            self.names[i].insertBefore(x, name)
    
    def getMasterScores(self, funcType):
        if funcType=="+":
            return self.scores[0]
        elif funcType == "-":
            return self.scores[3]
        elif funcType == "x":
            return self.scores[2]
        elif funcType == "÷":
            return self.scores[1]

    def getMasterNames(self, funcType):
        if funcType=="+":
            return self.names[0]
        elif funcType == "-":
            return self.names[3]
        elif funcType == "x":
            return self.names[2]
        elif funcType == "÷":
            return self.names[1]
    
    @staticmethod
    def createScores():
        masterScores = Linked()
        realdir = os.getcwd()
        print(os.getcwd())
        os.chdir(os.getcwd()+"/leaderboard/scores")
        for file in os.listdir():
            f = open(file,"r")
            subScores = Linked()
            for x in f:
                if x.endswith('\n'):
                    x = x[0:len(x)-1]
                subScores.insertTail(x)
            masterScores.insertTail(subScores)
            f.close()
        os.chdir(realdir)
        return masterScores

    @staticmethod
    def createNames():
        masterNames = Linked()
        realdir = os.getcwd()
        os.chdir(os.getcwd()+"/leaderboard/names")
        for file in os.listdir():
            subNames = Linked()
            f = open(file, "r")
            f.seek(0,2)
            times = f.tell()/3
            f.seek(0)
            for x in range(int(times)):
                subNames.insertTail(f.read(3))
            f.close()
            masterNames.insertTail(subNames)
        os.chdir(realdir)
        return masterNames