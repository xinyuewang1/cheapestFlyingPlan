'''
Created on 11 Apr 2018

@author: naomiwang
'''
import pandas as pd
import sys#,os
#THIS_DIR = os.path.dirname(os.path.abspath(__file__))
#print(THIS_DIR)

#from IPython.utils.py3compat import getcwd

#print(getcwd())
#pd.read_csv('../input/neatCountryCurrency.csv')

class CurrencyOfCountry:
    #__df = pd.read_csv('input/neatCountryCurrency.csv') 

    def __init__(self):
        self.__currencyOfCountry={}
    
    #def loadData(self,file=os.path.join(THIS_DIR,'input/neatCountryCurrency.csv')):    
    def loadData(self,file='input/neatCountryCurrency.csv'):
        self.__df = pd.read_csv(file)
        
        #neatDf=df.drop(["AirportID","AirportName","CityName","ICAOcode","Altitude","TimeOffset","DST","Tz"],1)
        try:
            self.__currencyOfCountry=self.__df.set_index("name").to_dict('index')
        except:
            sys.exit("[Error 2] Cannot parse "+file+". Please check the file directory or format.")
            
        return self.__df
    
    def getData(self):
        return self.__currencyOfCountry
    
    def getCurrency(self,country):
        # case sensitive
        try:
            return self.__currencyOfCountry[country]['currency_alphabetic_code']
        except KeyError:
            sys.exit("[Error 3] Invalid country name.")


# In[13]:


#cc = CurrencyOfCountry()
#cc.loadData()
#cc.getData()
#cc.getCurrency('China')

