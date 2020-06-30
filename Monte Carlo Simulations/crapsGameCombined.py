###The code below is based on Fig.16.2. in John Guttag's book. A 'shooter' has two options in a game of craps: i) Pass Line; and, ii) Do not Pass Line (dp)###
##The rules of the game for each choice are as follows:##
##Pass Line - shooter wins if he rolls 7 or 11;loses if he rolls 2, 3 or 12.Shooting anything else first becomes a 'pointer' and keeps rolling.To win the shooter must roll the 'pointer' again before he rolls a 7.
##
##Do not Pass Line - shooter loses if he rolls 7 or 11; wins for rolling 2 or 3. 12 is a tie, also known as push. Anything else becomes a point. Shooter must keep rolling until he rolls again to win. If he rolls a 7 before rolling a point, he loses. ##


##Objective --> Write a simulation to evaluate odds for each choice: i)Pass Line; or, ii)Do not Pass Line.##

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])


class CrapsGame(object):
    
    def __init__(self):
        """Initializing objects to 0"""
        self.passWins,self.passLosses=0,0
        self.dpWins,self.dpLosses,self.dpPushes=0,0,0

    def playHand(self):
        """Counts passWins, passLosses, dpWins, dpLosses and dpPushes"""
        throw=rollDie()+rollDie()
        if throw==7 or throw==11:
            self.passWins+=1
            self.dpLosses+=1
        elif throw==2 or throw==3 or throw==12:
            self.passLosses+=1
            if throw==2 or throw==3:
                self.dpWins+=1
            elif throw==12:
                self.dpPushes+=1
        else:
            point=throw
            while True:
                throw=rollDie()+rollDie()
                
                if throw==point:
                    self.passWins+=1
                    self.dpLosses+=1
                    break
                elif throw==7:
                    self.passLosses+=1
                    self.dpWins+=1
                    break
    
    def passResults(self):
        return (self.passWins,self.passLosses)
    def dpResults(self):
        return (self.dpWins,self.dpLosses,self.dpPushes)

##The code below is based on Fig. 16.3 in John Guttag's book. It needs the class CrapsGame from crapsGame.##

import random
from varStdDevCV import stdDev 

def crapsSim(handsPerGame,numGames):
    """Assumes handsPerGame and numGames are ints>0.
    Play numGames games of handsPerGame hands each; print results"""

    games=[]
    t,i=0,0
    #play numGames games#
    for t in range(numGames):
        c=CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)

    #Produce statistics for each game.#
    pROIPerGame,dpROIPerGame=[],[] #ROI for 'pass' and 'do not pass' lines.#
    for g in games:
        wins,losses=g.passResults()
        pROIPerGame.append((wins-losses)/float(handsPerGame))
        wins,losses,pushes=g.dpResults()
        dpROIPerGame.append((wins-losses)/float(handsPerGame))

    #Produce and print summary statistics#
    meanROI=str(round((100*sum(pROIPerGame)/numGames),4))+'%'
    sigma=str(round(stdDev(pROIPerGame),4))+'%'
    print('Pass Line:','Mean ROI = ',meanROI,'Std. Dev. = ',sigma)
    meanROI=str(round((100*sum(dpROIPerGame)/numGames),4))+'%'
    sigma=str(round(stdDev(dpROIPerGame),4))+'%'
    print('Do Not Pass Line:','Mean ROI = ', meanROI, 'Std. Dev. = ',sigma)


##Self-Check##
#handsPerGame=int(input('Enter number of hands per game: '))
#numGames=int(input('Enter number of games: '))
#crapsSim(handsPerGame,numGames)
print(crapsSim(10,10))
print(crapsSim(20,10))
print(crapsSim(1000,20))
print(crapsSim(100000,15))
