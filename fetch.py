'''
This is going to fetch the current csv files
from the internet
'''

import urllib.request

import time

import os

os.chdir('csvs')


_Now = int(time.time()  - 8)

_Start_Time = int(_Now - 31536000 - 8) 



#We need to convert time to date or whatever
URLS = {
	'ETH': f'https://query1.finance.yahoo.com/v7/finance/download/ETH-USD?period1={_Start_Time}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'BTC': f'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1={_Start_Time}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'DOGE' : f'https://query1.finance.yahoo.com/v7/finance/download/DOGE-USD?period1={_Start_Time}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'LTC' : f'https://query1.finance.yahoo.com/v7/finance/download/LTC-USD?period1={_Start_Time}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true'#aug 31 11:33:21
}

#href="https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1410825600&period2=1630368000&interval=1d&events=history&includeAdjustedClose=true"

URLS_ALL_TIME = {
	'ETH': f'https://query1.finance.yahoo.com/v7/finance/download/ETH-USD?period1=0&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'BTC': f'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=0&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'DOGE' : f'https://query1.finance.yahoo.com/v7/finance/download/DOGE-USD?period1=0&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'LTC' : f'https://query1.finance.yahoo.com/v7/finance/download/LTC-USD?period1=0&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true'#aug 31 11:33:21
}


URLS_6_MON = {
	'ETH': f'https://query1.finance.yahoo.com/v7/finance/download/ETH-USD?period1={_Now-15552000}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'BTC': f'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1={_Now-15552000}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'DOGE' : f'https://query1.finance.yahoo.com/v7/finance/download/DOGE-USD?period1={_Now-15552000}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true',
	'LTC' : f'https://query1.finance.yahoo.com/v7/finance/download/LTC-USD?period1={_Now-15552000}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true'#aug 31 11:33:21
}

#This gets us the most recent data from yahoo so that we can graph
for each in URLS:



	urllib.request.urlretrieve(URLS[each], f'{each}.csv')
for each in URLS_ALL_TIME:

	urllib.request.urlretrieve(URLS_ALL_TIME[each], f'{each}max.csv')

for each in URLS_6_MON:

	urllib.request.urlretrieve(URLS_6_MON[each], f'{each}6mon.csv')


def search_for_quote(symbol):

	try:

		year1url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={_Start_Time}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true'
		maxurl = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1=0&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true'
		mon6url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={_Now-15552000}&period2={_Now}&interval=1d&events=history&includeAdjustedClose=true'

		urllib.request.urlretrieve(year1url, f'{symbol}.csv')

		urllib.request.urlretrieve(maxurl, f'{symbol}max.csv')

		urllib.request.urlretrieve(mon6url, f'{symbol}6mon.csv')

		return True

	except:

		return False