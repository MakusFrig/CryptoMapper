'''
This is my crypto-mapper
'''
import csv

from tkinter import *

import fetch

import os

import setup_file

from tools import cc

root = Tk()

root.title("Crypto Mapper")

root.geometry("1600x900")

root.resizable(False, False)

root['bg'] = 'grey25'
	
DEFAULT_FONT = ('courier', 12)

CANVAS_WIDTH = 1450

CANVAS_HEIGHT = 750

#Here are some variables which are used in the graph crypto function

Timeline = '1 Year'

Current_Ticker = 'BTC'

Fill_In = True



Graph = Canvas(master = root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = 'black')

Graph.place(x = 150, y = 150)

Ticker_Chooser = Entry(master = root, font = DEFAULT_FONT, width = 16)

Ticker_Enter = Button(master = root, width = 13, text = 'Enter', font = DEFAULT_FONT, pady = -10,
	command = lambda:graph_crypto(Ticker_Chooser.get()), bg = 'grey')

Ticker_Chooser.place(x = 10, y = 10)

Ticker_Enter.place(x = 14, y = 40)

Name_Label = Label(master = root, text = '', bg = 'black', fg = 'yellow', font  = ('courier', 18))

Name_Label.place(x = 225, y = 155)

Min_Label = Label(master = root, bg = 'black', fg = 'red', font = ('courier', 6))

Max_Label = Label(master = root, bg = 'black', fg = 'red', font = ('courier', 6))

Mid_Label = Label(master = root, bg = 'black', fg = 'red', font = ('courier', 6))

Mid_Up_Label = Label(master = root, bg = 'black', fg = 'red', font = ('courier', 6))

Mid_Down_Label = Label(master = root, bg = 'black', fg = 'red', font = ('courier', 6))



Min_Label.place(x = 155, y = 820)

Max_Label.place(x = 155, y = 160)

Mid_Label.place(x = 155, y = 510)

Mid_Up_Label.place(x = 155, y = 300)

Mid_Down_Label.place(x = 155, y = 680)

#We also want to have a legend for the graph

Legend_Frame = LabelFrame(master = root, width = 145, height = 195, bg = 'grey25')

Legend = Text(master = Legend_Frame, width = 17, height = 11, bg = 'black', fg = 'white')

Legend.insert('1.0', 
"""Pink = Average
Blue = Avg Rise
Green = Raw Data""")

Legend.place(x = 0, y = 0)

Legend_Frame.place(x = 2, y = 700)


#This is for the label right here

def set_timeline(t):
	global Timeline

	Timeline = t

	graph_crypto(Current_Ticker)

Menu_Bar = Menu(master = root, bg = 'grey25')

Range_Menu = Menu(master = Menu_Bar, tearoff = 0, bg = 'grey25')

Range_Menu.add_command(label = '1 Year', command = lambda:set_timeline('1 Year'))

Range_Menu.add_command(label = 'MAX', command = lambda:set_timeline('MAX'))

Range_Menu.add_command(label = '6 Mon', command = lambda:set_timeline('6 Mon'))

Menu_Bar.add_cascade(label = 'Range', menu = Range_Menu)

#Next we want to be able to control the range in the ui

Range_Frame = LabelFrame(master = root, height = 100, width = 200, bg = 'grey25', text = 'Ranges')

One_Year = Button(master = Range_Frame, command = lambda:set_timeline('1 Year'), text = '1 Year', bg = 'grey25')

Max_Year = Button(master = Range_Frame, command = lambda:set_timeline('MAX'), text = 'MAX', bg = 'grey25', width = 3)

Six_Mon = Button(master = Range_Frame, command = lambda:set_timeline('6 Mon'), text = '6 Mon', bg = 'grey25')

Range_Frame.place(x = 1400, y = 90)

One_Year.grid(row = 1, column = 2)

Six_Mon.grid(row = 1, column = 1)

Max_Year.grid(row = 1, column = 3)

#We also want a button to toggle the fill

def toggle_fill():

	global Fill_In

	if Fill_In == False:

		Fill_In = True

	else:

		Fill_In = False

	graph_crypto(Current_Ticker)

Fill_Button = Button(master = root, text = 'Fill (TOGGLE)', command = toggle_fill, width = 13, bg = 'grey25')

Fill_Button.place(x = 1430, y = 50)

#This right here is for the information 

Info_Frame = LabelFrame(master = root, width = 500, height = 150, text = 'Information', bg = 'grey25')

High_Low = Text(master = Info_Frame, bg = 'grey25', width = 15)

High_Low.insert('1.0', 'High = \nLow = ')

Info_Frame.place(x = 200, y = 0)

High_Low.place(x = 0, y = 0)


def setup():

	global Graph

	

	#We want to draw the x and y axis

	Graph.create_line(50, (CANVAS_HEIGHT-50), CANVAS_WIDTH, (CANVAS_HEIGHT-50), fill = 'red')#X-axis

	Graph.create_line(50, (CANVAS_HEIGHT-50), 50, 0, fill ='red')#Y-axis

	Graph.create_line(50, (CANVAS_HEIGHT-50), 0, CANVAS_HEIGHT, fill = 'red')#This is just for nice UI

	#We also need to identify the different labels

	Graph.create_line(40, 10, 50, 0,fill = 'red')

	Graph.create_line(40, (CANVAS_HEIGHT-50)/4, 50, (CANVAS_HEIGHT-50)/4, fill = 'red')

	Graph.create_line(40, (CANVAS_HEIGHT-50)/2, 50, (CANVAS_HEIGHT-50)/2, fill = 'red')

	Graph.create_line(40, (CANVAS_HEIGHT-50)*3/4, 50, (CANVAS_HEIGHT-50)*3/4, fill = 'red')

	Graph.create_line(40, CANVAS_HEIGHT-60, 50, CANVAS_HEIGHT-50, fill = 'red')


	


def graph_crypto(ticker):

	global Graph, Ticker_Chooser

	global Timeline, Current_Ticker, Fill_In

	global Min_Label, Max_Label, Mid_Label, Mid_Up_Label, Mid_Down_Label

	global High_Low

	Graph.delete('all')

	setup()

	file_name = ''

	ticker = ticker.upper()

	for each_file in os.listdir():

		if ticker in each_file.split(".")[0]:

			Name_Label.config(text = ticker)

			if Timeline == '1 Year':

				file_name = ticker + ".csv"

			elif Timeline == 'MAX':

				file_name = ticker + "max.csv"

			elif Timeline == '6 Mon':

				file_name = ticker + "6mon.csv"

			break

	if file_name == '':

		if fetch.search_for_quote(ticker):

			print(os.listdir())

			for each_file in os.listdir():

				if ticker in each_file.split(".")[0]:

					Name_Label.config(text = ticker)

					if Timeline == '1 Year':

						file_name = ticker + ".csv"

					elif Timeline == 'MAX':

						file_name = ticker + "max.csv"

					elif Timeline == '6 Mon':

						file_name = ticker + "6mon.csv"

					break

			#This is just a fail-safe

			if file_name == '':

				return

		else:

			Ticker_Chooser.delete(0, 'end')

			Ticker_Chooser.insert(0, 'File Not Found')

			return

	#after this point we have effectivly found our csv file

	Current_Ticker = ticker



	file = open(file_name, 'r')

	file = list(csv.reader(file))

	for each_line in range(len(file)):

		file[each_line] = file[each_line][4]

	file = file[1:]

	#We want to ge thte average price

	average = 0

	#We want to convert all the numbers from string into floats

	for each_line in range(len(file)):

		if file[each_line] != 'null':
			file[each_line] = float(file[each_line])

			average += file[each_line]
		else:

			file[each_line] = 0.0
	average = average/len(file)

	min_price = 10000000

	max_price = 0

	for each_line in file:

		if each_line == 0:

			continue

		if each_line < min_price:

			min_price = each_line

		if each_line > max_price:

			max_price = each_line

	#We need to set some labels here now that we have this information

	High_Low.delete('1.0', END)

	High_Low.insert('1.0', f'High = {round(max_price, 2)}\nLow = {round(min_price, 2)}')

	#Here is where we graph

	#We need this for graphing

	yrange = max_price - min_price

	for each_line in range(1, len(file)):

		if file[each_line] == 0:

			continue

		#We need to be graphing relative to the amount of data



		x1 = int((CANVAS_WIDTH-50)*each_line/len(file))+50

		y1 = int((CANVAS_HEIGHT-50)*(file[each_line] - min_price)/yrange)

		searching = True

		counter = 1

		while searching:

			if file[each_line - counter] != 0:

				x2 = int((CANVAS_WIDTH-50)*(each_line-counter)/len(file))+50

				y2 = int((CANVAS_HEIGHT-50)*(file[each_line-counter] - min_price)/yrange)

				searching = False

			counter += 1

		#Here we want to graph from the last one to this one

		Graph.create_line(x1, cc(y1, CANVAS_HEIGHT-50), x2, cc(y2, CANVAS_HEIGHT-50), fill = 'green')

		if Fill_In:

			poly_coords = [x1, cc(y1, CANVAS_HEIGHT-50), x2, cc(y2, CANVAS_HEIGHT-50), x2, CANVAS_HEIGHT-50, x1, CANVAS_HEIGHT-50]

			Graph.create_polygon(poly_coords, fill = 'DeepPink2')

	#Now we want to show the average increase/decrease in price

	x1, x2 = 50, CANVAS_WIDTH

	y1, y2 = int((CANVAS_HEIGHT-50)*(file[0]-min_price)/yrange), int((CANVAS_HEIGHT-50)*(file[len(file)-1]-min_price)/yrange)

	#Now we graph

	Graph.create_line(x1, cc(y1, CANVAS_HEIGHT-50), x2, cc(y2, CANVAS_HEIGHT-50), fill = 'blue')

	#we also want to show the average price

	y = int((CANVAS_HEIGHT-50)*(average-min_price)/yrange)

	Graph.create_line(50, cc(y, CANVAS_HEIGHT-50), CANVAS_WIDTH, cc(y, CANVAS_HEIGHT-50), fill = 'purple')

	#We also need to update the graph numbers

	Min_Label.config(text = round(min_price, 1))

	Max_Label.config(text = round(max_price, 1))

	Mid_Label.config(text = round(average, 1))

	Mid_Up_Label.config(text = round((average+max_price)/2, 1))

	Mid_Down_Label.config(text = round((average+min_price)/2, 1))


	
	
	return

	

setup()

setup_file.setup_buttons(root, graph_crypto)
root.config(menu = Menu_Bar)


root.mainloop()