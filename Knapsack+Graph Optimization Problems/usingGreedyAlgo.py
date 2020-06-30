##Functions to use "greedy algorithm" to choose items. Their implementation is dependent on class 'Item' and function 'greedy'. Code is based on Fig.12.4. in John Guttag's book.##

from classItem import Item
from classItem import value,weightInverse,density
from greedyAlgorithm import greedy

def buildItems():
    names=['AB','CD','EF','GH','IJ','KL','MN']  #'names','values' and 'weights' are parameters passed to class 'Item' to build each element of list 'Items'#
    values=[1,2,3,4,5,6,7]
    weights=[5,10,15,20,25,30,35]
    Items=[]    #declaring empty list#
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))   #'Items' is a list declared earlier in the function.'Item' is a class imported from classItem.#
    return Items


def testGreedy(items,maxWeight,keyFunction):
    taken,val=greedy(items,maxWeight,keyFunction)
    print('total value of items taken is',val)
    for item in taken:
        print('  ',item)


def testGreedys(maxWeight=20):
    items=buildItems()
    print('Use greedy algorithm by value to fill a knapsack. maxWeight',maxWeight)
    testGreedy(items,maxWeight,value)
    print('Greedy algorithm by inverse of weight. maxWeight',maxWeight)
    testGreedy(items,maxWeight,weightInverse)
    print('Greedy algorithm by density(i.e. value:weight). maxWeight',maxWeight)
    testGreedy(items,maxWeight,density)

testGreedys()
