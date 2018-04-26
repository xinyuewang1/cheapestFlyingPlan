'''
Created on 20 Apr 2018

@author: naomiwang
'''
import pandas as pd
import sys#,os
#THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class Aircraft:
    def __init__(self):
        self.__crafts={}
        self.__df=None
    
    def loadData(self,file='input/aircraft.csv'):
        if file == 'input/aircraft.csv':
            self.__df = pd.read_csv(file,names=["code","type","units","manufacturer","range"])
            #print("I made it.")
        else:
            self.__df = pd.read_csv(file)
        try:
            self.__crafts=self.__df.set_index("code").to_dict('index')
        except:
            sys.exit("[Error 2] Cannot parse "+file+". Please check the file directory or format.")
            raise
        #return self.__df
            
    def getCrafts(self):
        return self.__crafts
    
    def getRange(self,code):
        # case insensitive
        code = code.upper()
        try:
            info = self.__crafts[code]
            units = info['units']
            ran = int(info['range'])
            if units == 'imperial':
                ran *= 1.60934
            return ran
        except KeyError:
            raise 
            sys.exit("[Error 3] class Aircraft- getRange- Invalid aircraft code.")
            
    def planeSet(self):
        return frozenset(self.__df['code'])
    