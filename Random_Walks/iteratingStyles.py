###The code below automates the process of chosing chart/plot styles###

class styleIterator(object):
    def __init__(self,styles):
        self.index=0
        self.styles=styles

    def getStyle(self):
        return self.styles

    def nextStyle(self):
        result=self.styles[self.index]
        if self.index==len(self.styles)-1:
            self.index=0
        else:
            self.index+=1
        
        return result
