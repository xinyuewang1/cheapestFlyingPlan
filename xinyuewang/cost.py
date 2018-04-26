'''
Created on 15 Apr 2018

@author: naomiwang
'''
import itertools,time
from xinyuewang.price import refuelCost
from xinyuewang.Graphs import RoutePriceSum

# timeit function Reference: https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts))
        else:
            print ('%r  %2.2f s' % \
                  (method.__name__, (te - ts)))
        return result

    return timed

def bestRoundTripV1(nodes):
    '''Semi brutal force.
    The idea is provide shortest distance as first and last leg.
    Then brute force the center possible routes and return the best(cheapest) route.
    Abandoned, because the last leg is wrong direction... = (
    '''
    
    start = nodes[0]
    distanceList = []
    for node in nodes[1:]:
        #print(node)
        pricy = refuelCost(start,node)
        distanceList.append([start,node,pricy])
    def minFunc(distanceNode):
        return distanceNode[2]
    min1 = min(distanceList[0],distanceList[1],key=minFunc)
    #print(min1)
    min2 = max(distanceList[0],distanceList[1],key=minFunc)
    for d in distanceList[2:]:
        if d[2] > min2[2]:
            pass
        elif d[2] < min1[2]:
            min1, min2 = d,min1
        else:
            min2 = d
    #print(min1,min2)
    restNodes = [i for i in nodes if i not in [start,min1[1],min2[1]]]
    allCombinations = list(itertools.permutations(restNodes,len(restNodes)))
    #print(allCombinations)
    resultList = []
    for mid in allCombinations:
        fullroute = [start,min1[1]]
        fullroute.extend(mid)
        fullroute+=[min2[1], start]
        #print(fullroute)
        routeSum = RoutePriceSum(fullroute)
        routePrice = routeSum.sumPrices()
        fullroute.append(routePrice)
        resultList.append(fullroute)
    #print(resultList)
    cheapest = resultList[0]
    for r in resultList[1:]:
        if r[-1]<cheapest[-1]:
            cheapest = r
            
    print("Cheapest route:",cheapest[:-1],"\nPrice:",cheapest[-1])
    
#bestRoundTripV1(['DUB','LHR','SYD','JFK','AAL'])
@timeit
def bestRoundTripV2(nodes):
    ''' Simple Greedy...'''
    
    route=[nodes[0]]
    distanceLib = []
    
    start = nodes.pop(0)
    while nodes:
        
        goto=[start,None,float("inf")]
        for node in nodes:
            #print(node)
            pricy = refuelCost(start,node)
            distanceLib.append([start,node,pricy])
            if goto[2] > pricy:
                goto = distanceLib[-1]
        #print(goto)
        route.append(goto[1])
        start = goto[1]
        nodes.remove(goto[1])
    
    route.append(route[0])
    p = RoutePriceSum(route)
        
    return route, p.sumPrices()

#print(bestRoundTripV2(['DUB','LHR','SYD','JFK','AAL']))

def distanceBlackBox(plane,nodes,aircraft,airportatlas):
    '''Permute all the possible links and provide for brutal force.'''
    
    limit = float("inf")
    
    #This section is to deal with the input line don't have a plane specified.
    if plane in aircraft.planeSet():
        limit = aircraft.getRange(plane)
        
    elif plane in airportatlas.airportSet():
        #No plane specified.
        nodes.append(plane)
    else:
        print("cost- distanceBlackBox- Invalid plane code.")
        return
    
    '''Here I break my route into two section, first is home to the nodes
    that can be reached by it (also means you can go back home from this
    nodes. Second, the nodes in between.
    I dump all the in between routes that have some place home cannot reach
    or end with it. e.g.: home A can only reach node B, C, D but not E. So
    I dump all the in between routes that start with E or end with E.
    Also those routes that have some in between distance too far for my plane.
    This makes what I feed into my price checking (which is the most expensive
    part of my program) is all possible routes.'''
     
    home = nodes[0]
    home_to = []
    possible2nd = []
    for x in nodes[1:]:
        d = airportatlas.getDistanceBetweenAirports(home,x)
        
        if d <= limit:
            home_to.append([home,x,d])
            possible2nd.append(x)
    
    other = nodes[1:]
    combo = list(itertools.permutations(other,len(other)))
    restRoute = []
    for route in combo:
        for x in range(len(route)-1):
            d = airportatlas.getDistanceBetweenAirports(route[x],route[x+1])
            if d > limit:
                break
        else:
            restRoute.append(route)
    result=[]
    for r in restRoute:
        if r[0] in possible2nd and r[-1] in possible2nd:
            result.append(r)
    #with open('input/disDict.txt','a') as f:
    #    f.write(str(disDict))
    return result
                    

@timeit
def bestRoundTripV3(plane,nodes,aircraft,airportatlas,cc,ci,theDict,ll=False):
    '''Brutal force with saving!'''
    
    allCombinations = distanceBlackBox(plane, nodes,aircraft,airportatlas)
    if allCombinations == None:
        return
    home = nodes.pop(0)
    cheapestRoute=[]
    cheapestPrice=float("inf")
    for i in allCombinations:
        l=[home]
        l.extend(i)
        l.append(home)
        p = RoutePriceSum(l,airportatlas,cc,ci,theDict)[0]
        if p < cheapestPrice:
            cheapestRoute=l
            cheapestPrice=p
    if ll:
        returnedDict = RoutePriceSum(cheapestRoute,airportatlas,cc,ci,theDict)[1]
        return cheapestRoute,cheapestPrice,returnedDict
    return cheapestRoute,cheapestPrice
            