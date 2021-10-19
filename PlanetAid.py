#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# importing requirements #

from tkinter import *

from tkinter import messagebox

import random

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# customizing main window #

main = Tk()

main.title("Planet Aid")
main.iconbitmap("logo.ico")
main.geometry("750x675")

main.resizable( height = False , width = False )

main.configure( bg = "#E8484B" )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# required variables #

matches = [ "Smallest planet\nin solar system" , "Mercury" , "Hottest planet\nin solar system" , "Venus" , "Planet where\nlife exists" , "Earth" , "Second\nsmallest planet" , "Mars" , "Largest planet\nin solar system" , "Jupiter" , "Second\nlargest planet" , "Saturn" , "Planet with\nicy materials" , "Uranus" , "Planet with the\nmost powerful wind" , "Neptune" ]

check_dictionary = {}

for i in range( 0 , 16 , 2 ) :
	check_dictionary[ matches[i] ] = matches[ i+1 ]

for j in range( 1 , 16 , 2 ) :
	check_dictionary[ matches[j] ] = matches[ j-1 ]

random.shuffle( matches )

count = 0

match_list = []

match_dictionary = {}

final_dictionary = {}

global winner_count
winner_count = 0

global personal_best
personal_best = 0

global no_of_clicks
no_of_clicks = 0

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# menubar function #

def reset() :

	global count
	global match_list,final_dictionary
	global winner_count,no_of_clicks

	random.shuffle( matches )
	
	buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8 , button9 , button10 , button11 , button12 , button13 , button14 , button15 , button16 ]
	
	for btn in buttons:
		btn.config( text = "" )
		btn.config( bg = "SystemButtonFace" )
		btn.config( bg = "#E8484B" )
		btn.config( state = "normal" )

	no_of_clicks = 0

	no_of_clicks_label.config( text = "N\nO\n.\n\nO\nF\n\nC\nL\nI\nC\nK\nS\n-\n" + str( no_of_clicks ) )

	count = 0
	match_list = []
	match_dictionary = {}
	final_dictionary = {}
	winner_count = 0

def help() :

	messagebox.showinfo( "Help" , "This a Tile Matching game.\nThis game consist of 16 tiles.\nYou are allowed to pick a tile at a time\nthen the other.\nIf the tile you selected previously\nis equal to the current selected tile,\nThen you get one matching tile pair.\nLike wise you need to gather\n8 tile pairs to win the game.\nALL THE BEST..!" )

def about() :

	messagebox.showinfo( " About " , "<Developed by>\n\nVenkatSaiVikram" )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# tile function #

def pick( button , index ) :

	global count
	global match_list
	global match_dictionary
	global final_dictionary
	global game_label
	global winner_count
	global personal_best , no_of_clicks

	no_of_clicks += 1

	no_of_clicks_label.config( text = "N\nO\n.\n\nO\nF\n\nC\nL\nI\nC\nK\nS\n-\n" + str( no_of_clicks ) )

	if button["text"] == "" and count < 2 :
		button["text"] = matches[index]
		button["bg"] = "#000000"
		button["fg"] = "#FFFFFF"
		match_list.append(index)
		match_dictionary[button]=matches[index]
		count+=1

	if len(match_list) == 2 :
		final_dictionary[ list( match_dictionary.values() )[0] ] = list( match_dictionary.values() )[1]

		if check_dictionary[ list( final_dictionary.keys() )[0] ] == final_dictionary[ list( final_dictionary.keys() )[0] ] :

			for key in match_dictionary :
				key[ "state" ] = "disabled"
				key[ "bg" ] = "#FFFFFF"
				key[ "fg" ] = "#000000"

			count = 0
			match_list = []
			match_dictionary = {}
			final_dictionary = {}
			winner_count += 1

			if winner_count == 8 :
				messagebox.showinfo( "Winner" , "Congratulations ! You Won !" )

				if personal_best == 0 :
					personal_best = no_of_clicks
					personal_best_label.config( text = "P\nE\nR\nS\nO\nN\nA\nL\n\nB\nE\nS\nT\n-\n" + str( no_of_clicks ) )

				elif personal_best < no_of_clicks :
					personal_best = personal_best
					personal_best_label.config( text = "P\nE\nR\nS\nO\nN\nA\nL\n\nB\nE\nS\nT\n-\n" + str( personal_best ) )

				elif personal_best > no_of_clicks :
					personal_best = no_of_clicks
					personal_best_label.config( text = "P\nE\nR\nS\nO\nN\nA\nL\n\nB\nE\nS\nT\n-\n" + str( no_of_clicks ) )

				elif personal_best == no_of_clicks :
					personal_best = no_of_clicks
					personal_best_label.config( text = "P\nE\nR\nS\nO\nN\nA\nL\n\nB\nE\nS\nT\n-\n" + str( personal_best ) )

		else :

			messagebox.showinfo( "Incorrect" , "Incorrect Match..!" )

			for key in match_dictionary:
				key[ "text" ] = ""
				key[ "bg" ] = "#E8484B"
				key[ "fg" ] = "#000000"

			count = 0
			match_list = []
			match_dictionary = {}
			final_dictionary = {}

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# menubar #

menu = Menu( main )

main.config( menu = menu )

options_menu = Menu( menu )

options_menu.add_separator()

menu.add_cascade( label = "Options" , menu = options_menu )

options_menu.add_command( label = "Reset" , command = reset )

options_menu.add_command( label = "Help" , command = help )

options_menu.add_command( label = "About" , command = about )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# header line label #

header = Label( text = "-------------------------------------------------------------------" , font = ( "Consolas" , 26 ) , bg = "#E8484B" , fg = "#000000" )
header.place( x = -1 , y = 9 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# personal best label #

personal_best_label = Label(text="P\nE\nR\nS\nO\nN\nA\nL\n\nB\nE\nS\nT\n-\n"+str(personal_best),font = ("Consolas",24),bg="#E8484B")
personal_best_label.pack(side="left",padx=20)

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# P label #

p = Label( text = "P" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
p.place( x = 195 , y = 167 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 1 #

button1 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button1 , 0 ) )
button1.place( x = 70 , y = 60 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 2 #

button2 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button2 , 1 ) )
button2.place( x = 235 , y = 60 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# L label #

l = Label( text = "L" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
l.place( x = 360 , y = 167 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 3 #

button3 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button3 , 2 ) )
button3.place( x = 400 , y = 60 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 4 #

button4 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button4 , 3 ) )
button4.place( x = 565 , y = 60 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# A label #

a = Label( text = "A" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
a.place( x = 525 , y = 167 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 5 #

button5 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button5 , 4 ) )
button5.place( x = 70 , y = 205 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 6 #

button6 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button6 , 5 ) )
button6.place( x = 235 , y = 205 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# N label #

n = Label( text = "N" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
n.place( x = 195 , y = 310 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 7 #

button7 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button7 , 6 ) )
button7.place( x = 400 , y = 205 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 8 #

button8 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button8 , 7 ) )
button8.place( x = 565 , y = 205 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# E label #

e = Label( text = "E" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
e.place( x = 360 , y = 310 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 9 #

button9 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button9 , 8 ) )
button9.place( x = 70 , y = 345 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 10 #

button10 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button10 , 9 ) )
button10.place( x = 235 , y = 345 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# T label #

t = Label( text = "T" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
t.place( x = 525 , y = 310 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 11 #

button11 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button11 , 10 ) )
button11.place( x = 400 , y = 345 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 12 #

button12 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button12 , 11 ) )
button12.place( x = 565 , y = 345 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# A label #

a = Label( text = "A" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
a.place( x = 195 , y = 450 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 13 #

button13 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button13 , 12 ) )
button13.place( x = 70 , y = 480 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 14 #

button14 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button14 , 13 ) )
button14.place( x = 235 , y = 480 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# I label #

i = Label( text = "I" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
i.place( x = 365 , y = 450 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 15 #

button15 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button15 , 14 ) )
button15.place( x = 400 , y = 480 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# button 16 #

button16 = Button( main , text = "" , height = 7 , width = 15 , bg = "#E8484B" , bd = 3 , relief = "solid" , command = lambda : pick( button16 , 15 ) )
button16.place( x = 565 , y = 480 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# D label #

d = Label( text = "D" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
d.place( x = 525 , y = 450 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# no of clicks label #

no_of_clicks_label = Label( text = "N\nO\n.\n\nO\nF\n\nC\nL\nI\nC\nK\nS\n-\n" + str( no_of_clicks ) , font  = ( "Consolas" , 24 ) , bg = "#E8484B" )
no_of_clicks_label.pack( side = "right" , padx = 20 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# footer line label #

footer = Label( text = "-------------------------------------------------------------------" , font = ( "Consolas" , 26 ) , bg = "#E8484B"  , fg = "#000000" )
footer.place( x = -1 , y = 610 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------#

# entering mainloop #

main.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------------#