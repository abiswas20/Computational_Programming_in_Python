##The code below is based on Fig. 16.3 in John Guttag's book. It needs the class CrapsGame from crapsGame.##

import random
from varStdDevCV import stdDev 
from crapsGame import rollDie,CrapsGame 

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
            print(t,i)
        games.append(c)
        print(games)

    #Produce statistics for each game.#
    pROIPerGame,dpROIPerGame=[],[] #ROI for 'pass' and 'do not pass' lines.#
    for g in games:
        wins,losses=g.passResults()
        pROIPerGame.append((wins-losses)/float(handsPerGame))
        print(pROIPerGame)
        wins,losses,pushes=g.dpResults()
        dpROIPerGame.append((wins-losses)/float(handsPerGame))
        print(dpROIPerGame)

    #Produce and print summary statistics#
    print(pROIPerGame,dpROIPerGame)
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
print(crapsSim(10,20))
