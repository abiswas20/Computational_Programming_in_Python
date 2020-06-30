import random

class Drunk(object):
    """Assumes name is a string"""
    def __init__(self,name=None):
        self.name=name

    def __str__(self):
        if self!=None:
            return self.name
        return 'Anonymous'

class usualDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1)]
        return random.choice(stepChoices)
        return random.choice(stepChoices)
