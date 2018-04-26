'''
Created on 14 Apr 2018

@author: naomiwang
'''
from xinyuewang.AirportAtlas import AirportAtlas
from xinyuewang.price import refuelCost

class DistanceGraph:
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
    graph = DistanceGraph(route)
    atlas = AirportAtlas()
    atlas.loadData()
    for x in range(len(route)-1):
        graph.add_edge(route[x], route[x+1], atlas.getDistanceBetweenAirports(route[x],route[x+1]))
    return graph.getList()
    '''
    w = atlas.getDistanceBetweenAirports('DUB','LHR')
    graph.add_edge('DUB','LHR',w)
    
    for x in range(len(nodeList)-1):
        for y in range(x+1,len(nodeList)):
            graph.add_edge(nodeList[x], nodeList[y], atlas.getDistanceBetweenAirports(nodeList[x],nodeList[y]))
    #graph.print_str()
    #print(graph.neighbours('DUB'))
       
#print( 'DUB' not in ['DUB','LHR','SYD','JFK','AAL'] or 'def' not in ['DUB','LHR','SYD','JFK','AAL'])
'''
#print(distances(['DUB','LHR','SYD','JFK','AAL']))
    
class PriceGraph(DistanceGraph):
#directed graph with weighted edges   
 
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

#theDict = {}
        
class PriceGraphV2:
    '''Directed weighted graph, maybe better with a dictionary structure?'''
    #global theDict
    #print(cli.theDict)
    #print("In class PGV2",theDict)
    
    def __init__(self,listOfNodes,theDict):
        self.theDict=theDict
        # dict of dict {a:{b:1,c:2,...},b:...}
        for n in listOfNodes:
            if not self.theDict.get(n):
            #self.__my_adjacency_dict[n] = {}
                self.theDict[n]={}
                #print("Implementing empty {} for",n,"\n",theDict)
            
        self.__vertex_content = listOfNodes
    
#    def setAdjacency(self,dic):
        '''dic is a dictionary'''
#        self.__my_adjacency_dict.update(dic)
        
    def add_vertex(self,x):
        #self.__my_adjacency_dict[x]={}
        if not self.theDict.get(x):
            
            self.theDict[x]={}
        self.__vertex_content.append(x)
    
    def add_edge(self,x,y,weight):
        '''Strictly from x to y'''
        
        self.theDict[x][y] = weight
        #print(len(self.theDict))
            #theDict[x][y] = weight
        #print("Before write back:",theDict)
        
    '''
    def neighbours(self, x):
        #return self.__my_adjacency_dict[x].keys()
        return theDict[x].keys()
    
    def print_str(self):
        print("Nodes:",self.__vertex_content,"\nEdges:",self.__my_adjacency_dict)        
    
    def getVertex(self):
        return self.__vertex_content
    
    def getDict(self):
        return self.__my_adjacency_dict
    '''
    
def RoutePriceSum(route,airportatlas,cc,ci,theDict):
    '''Calculate the cost of a certain route. If it once calculated, don't calculate
    again.'''
    
    #global theDict
    
    #def __init__(self,route,airportatlas,cc,ci,theDict):
    #self.graph = PriceGraphV2(route,theDict)
    #self.__itineraries = route
    sum = 0
    for x in range(len(route)-1):
        #Already append empty dict in PriceGraphV2
        #print('theDict.get(route[x],{}).get(route[x+1])',theDict.get(route[x],{}).get(route[x+1]))
        if not theDict.get(route[x]) or not theDict.get(route[x],{}).get(route[x+1]):
            if not theDict.get(route[x]):
                theDict[route[x]] = {}
            #print("Not in the dict")
            p = refuelCost(route[x], route[x+1],airportatlas,cc,ci)
            sum += p
            #self.graph.add_edge(route[x], route[x+1], p)
            theDict[route[x]][route[x+1]] = p
            #print(len(cli.theDict))
            #print("Calculated new edge:",p)
        else:
            p=float(theDict[route[x]][route[x+1]])
            sum += p
    
    #print("1:",theDict)
    return sum,theDict
    
#p = RoutePriceSum(['DUB','LHR','SYD','JFK','AAL'])
#print(p.sumPrices())    
#print(p.pricesList())   
#print(prices(['DUB','LHR','SYD','JFK','AAL']))
