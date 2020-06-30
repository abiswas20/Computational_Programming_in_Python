from decisionTreeImplementation import smallTest, buildManyItems, bigTest

def fastMaxVal(toConsider,avail,memo={}):
    """Assumes toConsider is a list of items for consideration and avail being the additional weight that the knapsack can hold.
    'memo' is dictionary to keep track of solutions for [len(toConsider),avail]"""

    #case 1 - when memo has the corresponding maxVal#
    if (len(toConsider),avail) in memo:
        result=memo[(len(toConsider),avail)]

    #case 2 - when toConsider==[] and avail==0#
    elif toConsider==[] and avail==0:   #nothing to consider and knapsack filled to capacity#
        result=(0,())

    #case 3 - when toConsider[0].getWeight()>avail#
    elif toConsider[0].getWeight()>avail:   #left branch not possible#
        #Explore Right Branch Only#
        result=fastMaxVal(toConsider[1:],avail,memo)

    #case 4 - when toConsider[0].getWeight()<avail#
    else:
        nextItem=toConsider[0]  #first item in the list 'toConsider'#
        #Explore left branch#
        withVal,withToTake=fastMaxVal(toConsider[1:],avail-toConsider.getWeight(),memo)
        withVal+=nextItem.getValue()
        #Explore right branch#
        withoutVal,withoutToTake=fastMaxVal(toConsider[1:],avail,memo)

    #choose the optimal branch#
    if withVal>withoutVal:
        result=(withVal,withToTake+(nextItem,))
    else:
        result=(withoutVal,withoutToTake)

    #memo saves the optimum choice based on length of list 'toConsider' and avail#
    memo[(len(toConsider),avail)]=result
    
    #return statement#
    return result

items=buildManyItems(30,13,5)
print(items)
#fastMaxVal(items,53,memo={})
