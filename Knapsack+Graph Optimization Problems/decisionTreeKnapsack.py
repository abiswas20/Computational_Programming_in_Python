###The following code is based on Fig.13.5 in John Guttag's book.###


from classItem import Item

def maxVal(toConsider,avail):     #2nd and 4th argument in node specification#
    
    """toConsider is a list of items and avail is remaining capacity in terms of
    weight. Function returns a tuple of: the total value of a solution to the 0/1
    knapsack problem, and, the items of that solution."""       #doc-string# 

    if toConsider==[] or avail==0:
        result=(0,())   #no item to choose and no space in the knapsack either.#
    ##Explore right branch##
    elif toConsider[0].getWeight()>avail:   #first element in list 'toConsider' heavier than capacity in terms of weight#
        result=maxVal(toConsider[1:],avail)         #list of second element onwards in toConsider#

    else:
        nextItem=toConsider[0]  #i.e. take the first item when its weight is less than capacity#
        ##Explore left branch##
        ##Continuation of 'else'##
        withVal,withToTake=maxVal(toConsider[1:],avail-nextItem.getWeight())    #Left branch stands for taking nextItem. And when we choose nextItem, the available capacity decreases#
        withVal+=nextItem.getValue()    #adding up values to calculate total#
        ##Explore right branch##
        withoutVal,withoutToTake=maxVal(toConsider[1:],avail)   #nothing picked from toConsider and no change in avail#
        ##Choose more optimized branch##
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

