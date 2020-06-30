#This is based on Fig.12.5 in John Guttag's book.The zero-one knapsack problem can be generalized as: 
#i)each item is represented by a pair; 
#ii)the maximum weight the knapsack can carry is w; 
#iii)A vector I of length n representing the set of n available items; 
#iv) A vector V of same length,n, to indicate whether or not the item was chosen; 
#v) Maximize sum(V[i]*I[i]) with the constraint Sum(V[i]*I[i].weight<=w.
#The following code depends on class Item,functions in usingGreedyAlgo.py and a function on generating powerset (eg. genPowerset,Fig.9.6.).

def chooseBest(pset,maxWeight,getVal,getWeight):
    bestVal=0.0
    bestSet=None
    for items in pset:
        itemsVal=0.0
        itemsWeight=0.0
        for item in items:
            itemsVal+=getVal(item)
            itemsWeight+=getWeight(item)
    if itemsWeight<maxWeight and itemsVal>bestVal:
        bestVal=itemsVal
        bestSet=items
    return ("Items:",bestSet,"Value:",bestVal)

from usingGreedyAlgo import buildItems,testGreedy,testGreedys
from genPowerset import genPowerset
def testBest(maxWeight=20):
    items=buildItems()
    print('items:',items)
    pset=genPowerset(items)
    print('pset:',pset)
    print('Items:',Items)
    taken,val=chooseBest(pset,maxWeight,Items.getVal,Items.getWeight)
    print("Total value of items taken:",val)
    for item in items:
        print(item)

