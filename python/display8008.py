import _mysql
import time
import datetime
import math
import pygame
from Adafruit_LED_Backpack import SevenSegment

#initialize displays

#totalDisplay = SevenSegment.SevenSegment(address=0x70)
#totalDisplay.begin()

unclosedDisplay = SevenSegment.SevenSegment(address=0x70)
unclosedDisplay.begin()

#connect and query db for total, unclosed
db = _mysql.connect("localhost", "root", "password", "JBCACHE")
db.query("""SELECT * from cache""")
res = db.use_result()
row = res.fetch_row();
if row[0][0] == 'unclosed':
	unclosed = row[0][1]
else:
	total = row[0][1]
row = res.fetch_row();
if row[0][0] == 'unclosed':
	unclosed = row[0][1]
else:
	total = row[0][1]

#debug
print datetime.datetime.now()
print 'unclosed: ' + unclosed
print 'total: ' + total

#-----------display-------------------

#totalDisplay.clear()

#totalDisplay.set_digit(3, int(total) % 10) #ones
#totalDisplay.set_digit(2, int(int(total)/10) % 10) #tens
#totalDisplay.set_digit(1, int(int(total)/100) % 10) #hundreds
#totalDisplay.set_digit(0, int(int(total)/1000) % 10) #thousands
#totalDisplay.write_display()

unclosedDisplay.clear()

unclosedDisplay.set_digit(3, 8) #ones
unclosedDisplay.set_digit(2, 0) #tens
unclosedDisplay.set_digit(1, 0) #hundreds
unclosedDisplay.set_digit(0, 8) #thousands
unclosedDisplay.write_display()

#---------play osunds--------------
#pygame.mixer.init()
#pygame.mixer.music.load("tetrisb.mid")
#pygame.mixer.music.play()
