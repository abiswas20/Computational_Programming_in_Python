##The following code is based on Fig.16.4. in John Guttag's book. It uses table lookup to replace inner loop in playHand demonstrated in Fig.16.2.##
##The table stores the probability for each outcome that's not a 7, 2, 3 or 12.###

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])


class CrapsGame(object):
    def __init__(self):
        """InitialIzing objects to 0"""
        self.passWins,self.passLosses=0,0
        self.dpWins,self.dpLosses,self.dpPushes=0,0,0

    def playHand(self):
        """An alternate faster implementation of playHand"""
        pointsDict={4:1/3,5:2/5,6:5/11,8:5/11,9:2/5,10:1/3}     #probability of each outcome#
        throw=rollDie()+rollDie()                              #simulates random value for a throw (ie. result)#
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
            if random.random()<=pointsDict[throw]:   #point before 7.probability of picking random number is less than or equal to probability of throw.e.g. if throw==5 then, by definition, 5 is point.Condition decides if random number is less than or equal to probability of throwing 5.#
                self.passWins+=1
                self.dpLosses+=1
            else:                                   #7 before point#
                self.passLosses+=1
                self.dpWins+=1
