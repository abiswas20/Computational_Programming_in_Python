class randomWalk:
    """Abstraction to simulate brownian motion"""
    def __init__(self,cLocX,cLocY):
        self.cLocX = cLocX
        self.cLocY = cLocY

    def getCurrentLoc(self):
        return self.cLocX , self.cLocY
