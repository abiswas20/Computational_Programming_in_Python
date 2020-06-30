class randomWalk:    
    """Abstraction to simulate brownian motion."""
    def __init__(self,cLocX,cLocY):
        self.cLocX=cLocX
        self.cLocY=cLocY
        #self.cLoc=[self.cLocX,self.cLocY]
       # self.mX=mX
        #self.mY=mY
        #self.fLocX=self.cLocX+self.mX
        #self.fLocY=self.cLocY+self.mY
        #self.fLoc=[self.fLocX,self.fLocY]

 #   def currentLoc(self):
#        self.cLoc=[self.cLocX,self.cLocY]
    
    def getCurrentLoc(self):
        return self.cLocX , self.cLocY

#    def futureLoc(self):
#        self.fLoc=[self.fLocX,self.fLocY]

#    def getFutureLoc(self):
#        return self.fLoc

#    def distance(self):
#        self.dist=(self.mX**2+self.mY**2)**0.5
#        return self.dist

#    def finalPosition(self,n):
#        for i in range(n):
#            self.cLoc=
#            i+=1
##Self-Test Code##
#from classRandomWalk import randomWalk
#z=randomWalk(0,0)
#print(z.getcurrentLoc())
