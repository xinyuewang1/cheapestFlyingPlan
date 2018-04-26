# -*- coding: utf-8 -*-

"""Console script for xinyuewang."""

import sys, csv,os,traceback
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Caching....
theDict = {}
csv_file = open(os.path.join(THIS_DIR,'input/theDict.csv'), 'r')
reader = csv.DictReader(csv_file)
for row in reader:
    item = theDict.get(row["start"],dict())
    item[row['end']] = row['refuelCost']
    theDict[row['start']] = item
csv_file.close()
#print("0:",theDict)
        
import click
from xinyuewang import Aircraft,AirportAtlas,CurrencyInfo,CurrencyOfCountry,cost

@click.command()
@click.option('-i',prompt='Input file', default='tests/input/testInput2.csv',
              help='Input file for route calculation.')
@click.option('--ac',prompt='aircraft file', default='input/aircraft.csv',
              help='Mandatory Columns: code, units, range')
@click.option('--aa',prompt='airport atlas file', default='input/airport.csv',
              help='Mandatory Columns: AirportName, Country, Latitude, Longitude')
@click.option('--ci',prompt='CurrencyInfo file', default='input/currencyrates.csv',
              help='Mandatory Columns: CurrencyCode, toEUR')
@click.option('--cc',prompt='CurrencyOfCountry', default='input/neatCountryCurrency.csv',
              help='Mandatory Columns: name, currency_alphabetic_code')
@click.option('-o',prompt='Output file', default='output.csv',
              help='Output to a named file.')
@cost.timeit
def main(i,ac,aa,ci,cc,o):
    """Console script for xinyuewang."""
    
    #Initializing
    aircraft = Aircraft.Aircraft()
    aircraft.loadData(ac)
    airportatlas = AirportAtlas.AirportAtlas()
    airportatlas.loadData(aa)
    currencyinfo = CurrencyInfo.CurrencyInfo()
    currencyinfo.loadData(ci)
    countrycurrency = CurrencyOfCountry.CurrencyOfCountry()
    countrycurrency.loadData(cc)
    
    try:
        
        f = open(i,'r')
        lines = f.readlines()
        o = open(o,'w')
        owriter = csv.writer(o)
        rDict={}
        #print(lines[-1])
        for row in lines:
            row = [x.strip() for x in row.split(',')]
            cities = row[:-1]
            plane = row[-1] 
            if row == lines[-1]:
                result = cost.bestRoundTripV3(plane,cities,aircraft,airportatlas,countrycurrency,currencyinfo,
                                              theDict,False)
            else:
                result = cost.bestRoundTripV3(plane,cities,aircraft,airportatlas,countrycurrency,currencyinfo,
                                              theDict,True)
                rDict = result[2]
                #print("2:",rDict)
            if result == None:
                click.echo("Error line:",row)
            else:
                click.echo("="*55+"\nAirports: "+str(row[:-1]))
                click.echo("Airplane: "+plane+"\nBest route: "+str(result[0]))
                click.echo("Total cost: "+str(result[1]))
            
            owriter.writerow([result[0],result[1]])
        f.close()
        o.close()
       
       
        #theDict = .pricesList()
        #print("3:",rDict)
        csv_file = open(os.path.join(THIS_DIR,'input/theDict.csv'), 'w')
        writer = csv.writer(csv_file)
        writer.writerow(['start','end','refuelCost'])
        #print(rDict)
        for outter in rDict:
            for inner in rDict[outter]: 
                writer.writerow([outter,inner,rDict[outter][inner]])
        csv_file.close()
        
        return 0
    
    except:# Exception as e:
        traceback.print_exc()
        #sys.exit("cli: "+e)
        return -1




if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
