###Code below is based on Fig.14.2 in John Guttag's book. Together the two classes help simulate random walk by a drunk personal, e.g. the position and distance from the original position.###

from usualAndUnusual import Drunk, usualDrunk

class Location(object):
    """Class to deal with position and distance."""
    def __init__(self,x,y):
        """x and y are position coordinates."""
        self.x=x
        self.y=y

    def coordinates(self):
        return self.x, self.y
    
    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self,other):
        """other stands for new position"""
        ox,oy=other.x,other.y
        xDist=other.x - self.x
        yDist=other.y - self.y
        return (xDist**2 + yDist**2)**0.5

    def newCoordinate(self,other):
        return (other.x,other.y)

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'


class Field(object):

    def __init__(self):
        self.drunks={}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk]=loc

    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        xDist,yDist=drunk.takeStep()
        currentLocation=self.drunks[drunk]
        #use method 'move' to compute current location#
        self.drunks[drunk]=currentLocation.move(xDist,yDist)

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]
