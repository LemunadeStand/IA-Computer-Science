from linked import Linked
class Files():
    def __init__(self):
        pass
    def createMultScores():
        leaderScores = Linked()
        f = open("scoresmult.txt", "r")
        for x in f:
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