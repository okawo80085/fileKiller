# killer agent

from tkinter import messagebox as mb
import tkinter as tk

from killer import KILLER
import os
import sys
import random

root = tk.Tk()
root.withdraw()

me = os.path.abspath(os.path.basename(__file__))
loc = os.getcwd()

killer = KILLER('./test', me)

fireInTheHole = False

yes = True
no = False

titles = ['stop', 'just stop', 'why aren\'t you stopping?', 'it\'s time to stop']

warns = {'are you sure you want to format "{}"?'.format(loc):yes,
		'are you really sure you want to do this?':yes,
		'are you really really sure you want to do this?':yes,
		'do really want to this? i mean there is no coming back...':yes,
		'do you really want to do this so much? the files are gonna be gone forever':yes,
		'there is no way back from this, files are not moved to bin, they are gone forever, continue?':yes,
		'you want to stop maybe?':no,
		'maybe you need to reconsider?':no,
		'i\'ll give you 2 more tries, wanna stop?':no,
		'i\'ll give you 1 more try, wanna stop?':no,
		'damn dude, stop, this is not fun, the files are gonna be gone!':no,
		'you are really that desperate to destroy those files huh?':yes,
		'if you do this i\'ll make you watch, still want to destroy them?':yes,
		'how about you just stop?':no,
		'ffs man! i\'m trying to stop you from making a mistake! STOP!':no,
		'it\'s time to STOP! where are your parents?':no,
		'c\'mon dude, just stop, it won\'t hurt you!':no,
		'ok, thats it, you\'ve pissed me off, this is you LAST warning: STOP!':no,
		'this is you very last warning: STOP OR I WILL MAKE IT EXTRA SLOW JUST TO MAKE YOU SUFFER!!!':no,
		'if you do this, i just want you to know, i hate you. do it?':yes
		}

for que, rep in warns.items():
	inn = mb.askyesno(random.choice(titles), que)

	if inn != rep:
		mb.showinfo('good choice!', 'your files will be safe for now')
		#sys.exit()

mb.showwarning('last warning', 'all your files in\n"{}"\nwill be gone'.format(loc))

inn = mb.askyesno('last try, stop?', 'you won\'t get another chance')

if inn != no:
	mb.showinfo('good choice!', 'your files will be safe for now')
	#sys.exit()

mb.showinfo('that\'s it, you\'ve done it', 'congrats you\'ve reached the no return point,\ni will make you and your files suffer now,\nunless...')

mb.askyesno('stop maybe?', 'if you do this it\'s on you\ncontinue?')

mb.showinfo('lol', 'hahaha\ndid you really think that you can stop now?')
killer.pfr()
mb.showinfo('xD', 'lol\nbtw here is the guy who\'ll kill all those files of yours:\n{}'.format(killer))

opStat = 'false alarm?'
if fireInTheHole:
	opStat = killer()

#end
print ('\n\n')
opReport = '{:=^60}'.format(' report start ') + '\noperation status: {}'.format(opStat) + '\nagent stats after the operation:\n{}'.format(killer) + '\ndata destroyed in operation: {}'.format(killer.kills) + '\ntargets left: {}'.format(len(killer.Files) + len(killer.Folders)) + '\n{:=^60}'.format(' report end ')

mb.showinfo('thats it, have a bad day!', opReport)