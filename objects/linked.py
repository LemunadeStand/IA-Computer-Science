from collections import deque
class Linked(deque):
    def __init__(self,text=""):
        deque.__init__(self,text)
        self.size = deque.__len__(self)
    #Returns if list is empty
    def isEmpty(self):
        if(self.size<=0):
            return True
        else:
            return False
    #Returns first element
    def first(self):
        if(self.size<=0):
            return -1
        else:
            return self[0]
    #Returns last element
    def last(self):
        if(self.size<=0):
            return -1
        else:
            return self[self.size-1]
    #Returns element before "x" index
    def before(self, x):
        if(self.size<=0):
            return -1
        else:
            return self[x-1]
    #Returns element after "x" index
    def after(self, x):
        if(self.size<=0):
            return -1
        else:
            return self[x+1]
    #Adds element to front
    def insertHead(self, x):
        deque.appendleft(self, x)
        self.size+=1
    #Adds element to back
    def insertTail(self, x):
        deque.append(self, x)
        self.size+=1
    #Inserts element before "pos" index
    def insertBefore(self, pos, x):
        if pos==0:
            deque.appendleft(self, x)
        else:
            deque.insert(self, pos, x)
        self.size+=1
    #Inserts element after "pos" index
    def insertAfter(self, pos, x):
        deque.insert(self, pos+1,x)
        self.size+=1
    #Clears list to be empty
    def clearq(self):
        self.clear()
        self.size = 0
    