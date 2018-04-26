'''
Created on 11 Apr 2018

@author: naomiwang
'''
from xinyuewang.Airport import Airport
import pandas as pd
from math  import radians,acos, sin,cos
import sys

class AirportAtlas:
    '''All the information need to known about airports in a certain file'''
     
    def __init__(self):
        #atlas info stored in dictionary
        self.__atlas={}
        self.__df=None
    
    def loadData(self,file='input/airport.csv'):
        #Read in data from csv
        if file == 'input/airport.csv':
            self.__df = pd.read_csv(file,names=["AirportID","AirportName","CityName","Country","code","ICAOcode","Latitude", "Longitude","Altitude","TimeOffset","DST","Tz"])
            #print("I made it.")
        else:
            self.__df = pd.read_csv(file)
        
        try:
            self.__atlas=self.__df.set_index("code").to_dict('index')
        except:
            sys.exit("[Error 2] Cannot parse "+file+". Please check the file directory or format.")
            raise
    
    def getAtlas(self):
        #return the dictionary
        return self.__atlas
    
    def getAirport(self,code):
        #take an airport IATA code and return an airport class
        try:
            if len(code)!=3:
                raise KeyError
            # case insensitive
            code = code.upper()
            
            info = self.__atlas[code]
            #print(info)
            #{'Country': 'Afghanistan', 'Latitude': 34.210017, 'Longitude': 62.2283}
            return Airport(code,info['AirportName'],info['Country'],info['Latitude'],info['Longitude'])
        except KeyError as e:
            print("[Error 0] AirportAtlas - getAirport - Invalid airport code.",str(e))
            raise
    
            
        
    def greatCircleDist(self,lat1, long1, lat2, long2):
        #Calculate distance on earth between two locations
        lat1r = radians(90-lat1)
        lon1r = radians(long1)
        lat2r = radians(90-lat2)
        lon2r = radians(long2)
        d = acos(sin(lat1r)*sin(lat2r)*cos(lon1r-lon2r)+cos(lat1r)*cos(lat2r))*6371
        return d
    
    def getDistanceBetweenAirports(self,code1,code2):
        '''Take two airports by code and return the calculate between them'''
        airport1=self.getAirport(code1)
        airport2=self.getAirport(code2)
        #print("Airports are: ",airport1.code,airport2.code)
        lat1,lon1=airport1.lat, airport1.lon
        lat2,lon2=airport2.lat, airport2.lon
        #print("Positions:",lat1,lon1,lat2,lon2)
        return self.greatCircleDist(lat1,lon1,lat2,lon2)
    
    # search for an Airport by Airport Name
    def getAirportByName(self,name):
        # case sensitive for now
        
        code = self.__df.loc[self.__df['AirportName'] == name]['code'].item()
        #print(code)
        a = self.getAirport(code)
        return a
    
    def airportSet(self):
        '''return a frozenset of all airport codes'''
        return frozenset(self.__df['code'])
