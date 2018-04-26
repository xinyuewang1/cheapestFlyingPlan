'''
Created on 14 Apr 2018

@author: naomiwang
'''
from xinyuewang.AirportAtlas import AirportAtlas
from xinyuewang.price import refuelCost

class DistanceGraph:
    '''Undirected graph'''
    
    def __init__(self,listOfNodes):
        # List of list [[a,b,weight],[a,c,weight]...]
        
        self.__my_adjacency_dict = []
        self.__vertex_content = listOfNodes
    
    def setAdjacency(self,node):
        self.__my_adjacency_dict.append(node)
        
    def add_vertex(self,x):
        #self.__my_adjacency_dict
        self.__vertex_content.append(x)
    
    def add_edge(self,x,y,weight):
        found = False
        for edge in self.__my_adjacency_dict:
            if  x in edge and y in edge: 
                found = True
        if not found:
            self.__my_adjacency_dict.append([x,y,weight])
        
    def neighbours(self, x):
        neighboursList = []
        for edge in self.__my_adjacency_dict:
            if x in edge:
                neighboursList.append(edge)
        return neighboursList
    
    def print_str(self):
        print("Nodes:",self.__vertex_content,"\nEdges:",self.__my_adjacency_dict)        
    
    def getVertex(self):
        return self.__vertex_content
    
    def getList(self):
        return self.__my_adjacency_dict
 
def distances(route):
    '''A function that takes a certain route and calculate the distance
    between each nodes. Return a list of list contain all the connecting
    information''' 
    graph = DistanceGraph(route)
    atlas = AirportAtlas()
    atlas.loadData()
    for x in range(len(route)-1):
        graph.add_edge(route[x], route[x+1], atlas.getDistanceBetweenAirports(route[x],route[x+1]))
    return graph.getList()
    
class PriceGraph(DistanceGraph):
    '''directed graph with weighted edges, inheritance from undirected
    graph'''   
 
    def add_edge(self,x,y,weight):
        found = False
        for edge in self.getList():
            if  x == edge[0] and y == edge[1]: 
                found = True
        if not found:
            self.setAdjacency([x,y,weight])
        
    def neighbours(self, x):
        neighboursList = []
        for edge in self.getList():
            if x == edge[0]:
                neighboursList.append(edge)
        return neighboursList
        
class PriceGraphV2:
    '''Directed weighted graph, maybe better with a dictionary structure?'''
    
    def __init__(self,listOfNodes,theDict):
        '''take theDict from cli and populate empty inner dictionary if
        some nodes is not yet available as a key in outter dictionary'''
        self.theDict=theDict
        # dict of dict {a:{b:1,c:2,...},b:...}
        for n in listOfNodes:
            if not self.theDict.get(n):
                self.theDict[n]={}
        self.__vertex_content = listOfNodes
            
    def add_vertex(self,x):
        '''add link if it's not in theDict'''
        if not self.theDict.get(x):
            self.theDict[x]={}
        self.__vertex_content.append(x)
    
    def add_edge(self,x,y,weight):
        '''Strictly from x to y'''
        
        self.theDict[x][y] = weight
    
def RoutePriceSum(route,airportatlas,cc,ci,theDict):
    '''Calculate the cost of a certain route. If it once calculated, don't calculate
    again.
    It's not actually necessary to use a graph...'''
    
    costSum = 0
    for x in range(len(route)-1):
        
        if not theDict.get(route[x]) or not theDict.get(route[x],{}).get(route[x+1]):
            if not theDict.get(route[x]):
                theDict[route[x]] = {}
            p = refuelCost(route[x], route[x+1],airportatlas,cc,ci)
            costSum += p
            theDict[route[x]][route[x+1]] = p

        else:
            p=float(theDict[route[x]][route[x+1]])
            costSum += p
    
    return costSum,theDict
