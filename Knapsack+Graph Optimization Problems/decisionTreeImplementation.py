###The following code is based on Fig.13.6 in John Guttag's book. It is an implementation of decision tree based implementation that draws in 'maxVal()' defined previously.###

import random
from classItem import Item
from decisionTreeKnapsack import maxVal

##smallTest() generates random set to represent Items##
def smallTest():
    names=['a','b','c','d']
    vals=[6,7,8,9]
    weights=[3,3,2,5]
    Items=[]

    for i in range (len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))

    val,taken=maxVal(Items,5)

    for item in taken:
        print(item)
    print('Total value of the items taken=',val)


##buildManyItems(numItems,maxVal,maxWeight) constructs "numItems" sets of items.##
def buildManyItems(numItems,maxVal,maxWeight):
    items=[]
    for i in range(numItems):
        items.append(Item(str(i),random.randint(0,maxVal),random.randint(0,maxWeight)))
    return items
       
##def bigTest(numItems) returns the items that should be taken from the randomly generated Items.##
def bigTest(numItems):
    items=buildManyItems(numItems,10,10)
    val,taken=maxVal(items,40)
    for item in taken:
        print(items)
    print("Total value of items taken = ",val)


print(bigTest(25))
