class Digraph(object):
    

    def __init__(self,nodes,edge):
        self.nodes=[]
        self.edges={}


    def addNode(self,node):
        if node in self.nodes:
            raise ValueError('node already exists')
        else:
            self.node.append(node)
            self.edges[node]=[]

    def addEdge(self,edge):
        self.edges.append(src.getName()+'->'+dest.getName())

    def childrenOf(self,node):


    def hasNode(self,node):

    def __str__(self):
        result=''
        for src in self.node:
            for dest in self.edge[src]:
                result=result + src.getName() + '->' + dest.getName() + '\n'
                return result[:-1]

