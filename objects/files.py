from objects.linked import Linked
import os
class Files():
    def __init__(self, scores, names):
        self.scores = [scores[0], scores[1], scores[2], scores[3]]
        self.names = [names[0], names[1], names[2], names[3]]
    
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
        #Goes through all files in scores folder
        for file in os.listdir():
            f = open(file, "w")
            #Writes new scores in specified format "score,time"
            for x in self.scores[i]:
                f.write(x[0]+","+x[1]+"\n")
            f.close()
            i+=1
        i = 0
        os.chdir(realdir+"/leaderboard/names")
        #Goes through all files in names folder
        for file in os.listdir():
            f = open(file, "w")
            #Writes new names in one long string
            for x in self.names[i]:
                f.write(x)
            f.close()
            i+=1
    
    def add(self, funcType, score, time, name):
        x=0
        i=0
        #Decide which linnked list based on operation
        if funcType=="+":
            i=0
        elif funcType=="-":
            i=3
        elif funcType=="x":
            i=2
        elif funcType=="÷":
            i=1
        #Linearly searches through linked list
        while x<self.scores[i].size and score<int(self.scores[i][x][0]):
            x+=1
        #Adds entry to end if gone through entire list
        if x==self.scores[i].size:
            self.scores[i].insertTail(tuple([str(score), str(time)]))
            self.names[i].insertTail(name)
        #Inserts entry where it should be
        else:
            self.scores[i].insertBefore(x, tuple([str(score), str(time)]))
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
        masterScores = []
        realdir = os.getcwd()
        os.chdir(os.getcwd()+"/leaderboard/scores")
        #Go through all function types files
        for file in os.listdir():
            #Read from file
            f = open(file,"r")
            #Subscores and times per functype
            subScores = Linked()
            subTimes = Linked()
            for x in f:
                if x.endswith('\n'):
                    x = x[0:len(x)-1]
                subScores.insertTail(x[0:x.index(',')])
                subTimes.insertTail(x[x.index(',')+1:])
            joinScoresTimes = Linked()
            #Merge scores and times
            for x in range(subScores.size):
                joinScoresTimes.insertTail(tuple([subScores[x], subTimes[x]]))
            masterScores.append(joinScoresTimes)
            f.close()
        os.chdir(realdir)
        return masterScores

    @staticmethod
    def createNames():
        masterNames = []
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
            masterNames.append(subNames)
        os.chdir(realdir)
        return masterNames