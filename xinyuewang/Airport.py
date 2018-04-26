'''
Created on 11 Apr 2018

@author: naomiwang
'''
class Airport:
    def __init__(self,code,name,country,lat,lon):
        self.code=code
        self.name=name
        self.country=country
        self.lat=lat
        self.lon=lon
        
    @property
    def code(self):
        return self.__code
    @code.setter
    def code (self,val):
        self.__code = val
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,val):
        self.__name = val
       
    def __str__(self):
        return 'Code: '+str(self.code)+', Name: '+self.name+', Country: '+self.country+', Lat: '+str(self.lat)+', Lon: '+str(self.lon)
 