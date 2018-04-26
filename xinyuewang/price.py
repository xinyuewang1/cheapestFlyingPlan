'''
Created on 11 Apr 2018

@author: naomiwang
'''

def refuelCost(code1,code2,airportatlas,cc,ci):
    '''refuelCost = distance * fuelcost'''
    
    #Changed here from code1 to code2, which means refuel at destination country
    country = airportatlas.getAirport(code2).country
    currencyCode = cc.getCurrency(country)
    currencyRate = ci.getCurrencyRate(currencyCode)
    distance = airportatlas.getDistanceBetweenAirports(code1, code2)
    return currencyRate*distance
    