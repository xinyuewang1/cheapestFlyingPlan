'''
Created on 11 Apr 2018

@author: naomiwang
'''
import  pandas as pd
import sys

class CurrencyInfo: 
    
    def __init__(self):
        self.__currencyInfo={}
    
    def loadData(self,file='input/currencyrates.csv'):
        if file == 'input/currencyrates.csv':
            self.__df = pd.read_csv(file,names=["CountryName","CurrencyCode","toEUR","EURto"])
            #print(__df)
        else:
            self.__df = pd.read_csv(file)
        try:
            self.__currencyInfo=self.__df.set_index("CurrencyCode").to_dict('index')
        except Exception as e :
            print(e)
            sys.exit("[Error 2] Cannot parse "+file+". Please check the file directory or format.")
        return self.__df
    
    def getCurrencyInfo(self):
        return self.__currencyInfo
    
    def getCurrencyRate(self,code):
        try:
            if len(code)!=3:
                raise KeyError
            # case insensitive
            code = code.upper()
            
                #info = self.__currencyInfo[code]
            return self.__currencyInfo[code]['toEUR']
        except KeyError:
            print("[Error 1]CurrencyInfo- getCurrencyRate- Invalid currency code.")
            raise
    
