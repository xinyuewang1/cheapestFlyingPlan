'''
Created on 11 Apr 2018

@author: naomiwang
'''
import pandas as pd
import sys

class CurrencyOfCountry:
    '''The class store info of country name and the currency of it''' 

    def __init__(self):
        self.__currencyOfCountry={}
        
    def loadData(self,file='input/neatCountryCurrency.csv'):
        self.__df = pd.read_csv(file)
        
        try:
            self.__currencyOfCountry=self.__df.set_index("name").to_dict('index')
        except:
            sys.exit("[Error 2] Cannot parse "+file+". Please check the file directory or format.")
    
    def getData(self):
        return self.__currencyOfCountry
    
    def getCurrency(self,country):
        '''Input country name, return the currency code'''
        # case sensitive
        try:
            return self.__currencyOfCountry[country]['currency_alphabetic_code']
        except KeyError:
            print ("[Error 3] Invalid country name.")
            raise
