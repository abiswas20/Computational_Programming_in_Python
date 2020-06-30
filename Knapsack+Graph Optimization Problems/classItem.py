##The following code is based on Fig.12.2. in John Guttag's book. Class Item defines name, value and weight attribute for each item.##

class Item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=v
        self.weight=w
    
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result='<'+self.name+','+str(self.value)\
                +','+str(self.weight)+'>'
        return result

##The following are functions based on class Item above##
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()
