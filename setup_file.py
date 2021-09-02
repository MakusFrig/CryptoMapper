'''
This is the setup file for my crypto display
'''

from tkinter import Button

def setup_buttons(frame, function):
	#In this function we want to make buttons which auto display 
	#The verious cryptos onto the graphs

	_Btc = Button(master = frame, text = 'BITCOIN', command = lambda:function('BTC'), width = 15, bg = 'grey', padx = 12)

	_Eth = Button(master = frame, text = 'ETHEREUM', command = lambda:function('ETH'), width = 15, bg = 'grey', padx = 12)

	_Doge = Button(master = frame, text = 'DOGECOIN', command = lambda:function('DOGE'), width = 15, bg = 'grey', padx = 12)

	_Ltc = Button(master = frame, text = 'LITECOIN', command = lambda:function('LTC'), width = 15, bg = 'grey', padx = 12)

	_Btc.place(x = 0, y = 150)

	_Eth.place(x = 0, y = 180)

	_Doge.place(x = 0, y = 210)

	_Ltc.place(x =0, y = 240)

	return