##The following code is an implementation of Greedy Algorithm based on Fig.12.3. in John Guttag's book.## 

from classItem import Item

def greedy(items,maxWeight,keyFunction):    #items is a list,maxWeight is the maximum capacity, keyFunction is key for sorting#
    """Assumes Items is a list, maxWeight>=0
    keyFunction maps elements of Items to numbers."""
    itemsCopy=sorted(items,key=keyFunction,reverse=True)    #sort in reverse order wrt keyFunction#
    result=[]   #declare empty
    totValue=0.0
    totWeight=0.0
    for i in range(len(itemsCopy)):
        if (totWeight+itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totValue+=itemsCopy[i].getValue()
            totWeight+=itemsCopy[i].getWeight()
    return (result,totValue)
