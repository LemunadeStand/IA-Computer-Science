from linked import Linked
class Files():
    #XS is "X" function scores and XN is "X" function name
    def __init__(self, AS, AN, SS, SN, MS, MN, DS, DN):
        self.AS = AS
        self.AN = AN
        self.SS = SS
        self.SN = SN
        self.MS = MS
        self.MN = MN
        self.DS = DS
        self.DN = DN
    
    def clear(self):
        self.AS = Linked()
        self.AN = Linked()
        self.SS = Linked()
        self.SN = Linked()
        self.MS = Linked()
        self.MN = Linked()
        self.DS = Linked()
        self.DN = Linked()
        f = open("scoresadd.txt","w")
        f.write("")
        f.close()
        f = open("scoressub.txt","w")
        f.write("")
        f.close()
        f = open("scoresmult.txt","w")
        f.write("")
        f.close()
        f = open("scoresdiv.txt","w")
        f.write("")
        f.close()
        f = open("leaderboardadd.txt","w")
        f.write("")
        f.close()
        f = open("leaderboardsub.txt","w")
        f.write("")
        f.close()
        f = open("leaderboarddiv.txt","w")
        f.write("")
        f.close()
        f = open("leaderboardmult.txt","w")
        f.write("")
        f.close()

    def save(self):
        f = open("scoresadd.txt","w")
        for i in self.AS:
            f.write(i+"\n")
        f.close()
        f = open("leaderboardadd.txt","w")
        for i in self.AN:
            f.write(i)
        f.close()

        f = open("scoressub.txt","w")
        for i in self.SS:
            f.write(i+"\n")
        f.close()
        f = open("leaderboardsub.txt","w")
        for i in self.SN:
            f.write(i)
        f.close()

        f = open("scoresmult.txt","w")
        for i in self.MS:
            f.write(i+"\n")
        f.close()
        f = open("leaderboardmult.txt","w")
        for i in self.MN:
            f.write(i)
        f.close()

        f = open("scoresdiv.txt","w")
        for i in self.DS:
            f.write(i+"\n")
        f.close()
        f = open("leaderboarddiv.txt","w")
        for i in self.DN:
            f.write(i)
        f.close()
    
    def add(self, funcType, score, name):
        x=0
        if funcType =="+":
            while x<self.AS.size and score>float(self.AS[x]):
                x+=1
            if x==self.AS.size:
                self.AS.insertTail(str(score))
                self.AN.insertTail(name)
            else:
                self.AS.insertBefore(x, str(score))
                self.AN.insertBefore(x, name)
        elif funcType == "-":
            while x<self.SS.size and score>float(self.SS[x]):
                x+=1
            if x==self.SS.size:
                self.SS.insertTail(str(score))
                self.SN.insertTail(name)
            else:
                self.SS.insertBefore(x, str(score))
                self.SN.insertBefore(x, name)
        elif funcType == "x":
            while x<self.MS.size and score>float(self.MS[x]):
                print(self.MS[x]+"<"+str(score))
                x+=1
            if x==self.MS.size:
                self.MS.insertTail(str(score))
                self.MN.insertTail(name)
            else:
                self.MS.insertBefore(x, str(score))
                self.MN.insertBefore(x, name)
        elif funcType == "÷":
            while x<self.DS.size and score>float(self.DS[x]):
                x+=1
            if x==self.DS.size:
                self.DS.insertTail(str(score))
                self.DN.insertTail(name)
            else:
                self.DS.insertBefore(x, str(score))
                self.DN.insertBefore(x, name)
    
    def getMasterScores(self, funcType):
        if funcType=="+":
            return self.AS
        elif funcType == "-":
            return self.SS
        elif funcType == "x":
            return self.MS
        elif funcType == "÷":
            return self.DS

    def getMasterNames(self, funcType):
        if funcType=="+":
            return self.AN
        elif funcType == "-":
            return self.SN
        elif funcType == "x":
            return self.MN
        elif funcType == "÷":
            return self.DN
    
    def createMultScores():
        leaderScores = Linked()
        f = open("scoresmult.txt", "r")
        for x in f:
            #account for last line which is blank
            if len(x)>3:
                x = x[0:len(x)-1]
                leaderScores.insertTail(x)
        f.close()
        return leaderScores

    def createMultNames():
        leaderNames = Linked()
        f = open("leaderboardmult.txt", "r")
        f.seek(0,2)
        times = f.tell()/3
        f.seek(0)
        for x in range(int(times)):
            leaderNames.insertTail(f.read(3))
        f.close()
        return leaderNames

    def createDivScores():
        leaderScores = Linked()
        f = open("scoresdiv.txt", "r")
        for x in f:
            if len(x)>3:
                x = x[0:len(x)-1]
                leaderScores.insertTail(x)
        f.close()
        return leaderScores

    def createDivNames():
        leaderNames = Linked()
        f = open("leaderboarddiv.txt", "r")
        f.seek(0,2)
        times = f.tell()/3
        f.seek(0)
        for x in range(int(times)):
            leaderNames.insertTail(f.read(3))
        f.close()
        return leaderNames

    def createAddScores():
        leaderScores = Linked()
        f = open("scoresadd.txt", "r")
        for x in f:
            if len(x) >3:
                x = x[0:len(x)-1]
                leaderScores.insertTail(x)
        f.close()
        return leaderScores

    def createAddNames():
        leaderNames = Linked()
        f = open("leaderboardadd.txt", "r")
        f.seek(0,2)
        times = f.tell()/3
        f.seek(0)
        for x in range(int(times)):
            leaderNames.insertTail(f.read(3))
        f.close()
        return leaderNames

    def createSubScores():
        leaderScores = Linked()
        f = open("scoressub.txt", "r")
        for x in f:
            if len(x)>3:
                x = x[0:len(x)-1]
                leaderScores.insertTail(x)
        f.close()
        return leaderScores

    def createSubNames():
        leaderNames = Linked()
        f = open("leaderboardsub.txt", "r")
        f.seek(0,2)
        times = f.tell()/3
        f.seek(0)
        for x in range(int(times)):
            leaderNames.insertTail(f.read(3))
        f.close()
        return leaderNames