from collections import deque
class Linked(deque):
    def __init__(self,text=""):
        deque.__init__(self,text)
        self.size = deque.__len__(self)
    def isEmpty(self):
        if(self.size<=0):
            return True
        else:
            return False
    def first(self):
        if(self.size<=0):
            return -1
        else:
            return self[0]
    def last(self):
        if(self.size<=0):
            return -1
        else:
            return self[self.size-1]
    def before(self, x):
        if(self.size<=0):
            return -1
        else:
            return self[x-1]
    def after(self, x):
        if(self.size<=0):
            return -1
        else:
            return self[x+1]
    def insertHead(self, x):
        deque.appendleft(self, x)
        self.size+=1
    def insertTail(self, x):
        deque.append(self, x)
        self.size+=1
    def insertBefore(self, pos, x):
        if pos==0:
            deque.appendleft(self, x)
        else:
            deque.insert(self, pos-1, x)
        self.size+=1
    def insertAfter(self, pos, x):
        deque.insert(self, pos+1,x)
        self.size+=1
    