__author__ = 'Ryan Stratton'
# this project was modifed from the sample provided by professor hornof and using information
# gained from experimentation and various sources, sources that provided useful to me are
# listed below

# additional resources used besides the ones provided by the professor

# https://daniweb.com/programming/software-development/code/216830/tkinter-keypress-event-python
# https://www.tutorialspoint.com/python/tk.pack.htm
# stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly


# I apologize for the long repetitive code, I was having some problems with getting it to work 
# and used repetitive code instead of using loops to better understand what was going on and 
# I ended up sticking with it instead of making function calls and loops. I understand its not 
# great code design but my main goal was understanding.


# Package imports
import readchar

# Local imports
from sound import Sound
from tkinter import *
from audioArray import *


#place holders for locations in the arrays of visual displays
ColorIndex = 0
DayIndex = 0
HourIndex = 0
AMorPM = 0
MinuteIndex = 0

#this class handles the selection of days
class Day:
	def __init__(self,parent):
		self.parent = parent
		self.frame = Frame(parent)

		if DayIndex == 0:
			self.Day1 = Label(self.parent, text = '   Monday   ', font=("Courier,22"), background = "green")
		else:
			
			self.Day1 = Label(self.parent, text = '   Monday   ', font=("Courier,22"), background = "white")

		self.Day1.pack(side = LEFT)
		self.Day1.bind("<Key>", self.DayKeyPress)		
		
		if DayIndex == 1:
			self.Day2 = Label(self.parent, text = '   Tuesday   ', font=("Courier,22"), background = "green")
		else:
			
			self.Day2 = Label(self.parent, text = '   Tuesday   ', font=("Courier,22"), background = "white")

		self.Day2.pack(side = LEFT)
		self.Day2.bind("<Key>", self.DayKeyPress)		

		if DayIndex == 2:
			self.Day3 = Label(self.parent, text = '   Wednesday   ', font=("Courier,22"), background = "green")
		else:
			
			self.Day3 = Label(self.parent, text = '   Wednesday   ', font=("Courier,22"), background = "white")

		self.Day3.pack(side = LEFT)
		self.Day3.bind("<Key>", self.DayKeyPress)		

		if DayIndex == 3:
			self.Day4 = Label(self.parent, text = '   Thursday   ', font=("Courier,22"), background = "green")
		else:
			self.Day4 = Label(self.parent, text = '   Thursday   ', font=("Courier,22"), background = "white")

		self.Day4.pack(side = LEFT)
		self.Day4.bind("<Key>", self.DayKeyPress)		
		
		if DayIndex == 4:
			self.Day5 = Label(self.parent, text = '   Friday   ', font=("Courier,22"), background = "green")
		else:
			self.Day5 = Label(self.parent, text = '   Friday   ', font=("Courier,22"), background = "white")

		self.Day5.pack(side = LEFT)
		self.Day5.bind("<Key>", self.DayKeyPress)		

		if DayIndex == 5:
			self.Day6 = Label(self.parent, text = '   Saturday   ', font=("Courier,22"), background = "green")
		else:
			self.Day6 = Label(self.parent, text = '   Saturday   ', font=("Courier,22"), background = "white")

		self.Day6.pack(side = LEFT)
		self.Day6.bind("<Key>", self.DayKeyPress)		

		if DayIndex == 6:
			self.Day7 = Label(self.parent, text = '   Sunday   ', font=("Courier,22"), background = "green")
		else:
			self.Day7 = Label(self.parent, text = '   Sunday   ', font=("Courier,22"), background = "white")
		
		self.Day7.pack(side = LEFT)
		self.Day7.bind("<Key>", self.DayKeyPress)		

		self.frame.pack()
		self.parent.bind("<Key>", self.DayKeyPress)

	#close the window
	def close_windows(self):
		self.parent.destroy()

	#what happens when j,k, or space is hit in the day menu
	def DayKeyPress(self,event):
		global DayIndex
		if event.keysym == 'space' or event.char == event.keysym:

			if event.char == 'j':
				if DayIndex == 0:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="green")
					Sounds = Sound( "wav_files/days_of_week_f/sunday_f.wav")
					Sounds.play()
					DayIndex = 6

				elif DayIndex == 1:
					self.Day1.configure(background ="green")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/monday_f.wav")
					Sounds.play()
					DayIndex = 0

				elif DayIndex == 2:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="green")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/tuesday_f.wav")
					Sounds.play()
					DayIndex = 1


				elif DayIndex == 3:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="green")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/wednesday_f.wav")
					Sounds.play()
					DayIndex = 2


				elif DayIndex == 4:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="green")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/thursday_f.wav")
					Sounds.play()
					DayIndex = 3


				elif DayIndex == 5:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="green")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/friday_f.wav")
					Sounds.play()
					DayIndex = 4


				elif DayIndex == 6:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="green")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/saturday_f.wav")
					Sounds.play()
					DayIndex = 5


			elif event.char == 'k':
				if DayIndex == 0:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="green")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/tuesday_f.wav")
					Sounds.play()
					DayIndex = 1


				elif DayIndex == 1:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="green")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/wednesday_f.wav")
					Sounds.play()
					DayIndex = 2


				elif DayIndex == 2:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="green")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/thursday_f.wav")
					Sounds.play()
					DayIndex = 3


				elif DayIndex == 3:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="green")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/friday_f.wav")
					Sounds.play()
					DayIndex = 4


				elif DayIndex == 4:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="green")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/saturday_f.wav")
					Sounds.play()
					DayIndex = 5


				elif DayIndex == 5:
					self.Day1.configure(background ="white")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="green")
					Sounds = Sound( "wav_files/days_of_week_f/sunday_f.wav")
					Sounds.play()
					DayIndex = 6


				elif DayIndex == 6:
					self.Day1.configure(background ="green")
					self.Day2.configure(background ="white")
					self.Day3.configure(background ="white")
					self.Day4.configure(background ="white")
					self.Day5.configure(background ="white")
					self.Day6.configure(background ="white")
					self.Day7.configure(background ="white")
					Sounds = Sound( "wav_files/days_of_week_f/monday_f.wav")
					Sounds.play()
					DayIndex = 0

			elif event.keysym == 'space':
				self.close_windows()





#the class that handles hour selection
class Hour:
	def __init__(self,parent):
		self.parent = parent
		self.frame = Frame(parent)
		
		if HourIndex == 0:
			self.Hour1 = Label(self.parent, text = '   1   ', font=("Courier,22"), background = "green")
		else:
			self.Hour1 = Label(self.parent, text = '   1   ', font=("Courier,22"), background = "white")

		self.Hour1.pack(side = LEFT)
		self.Hour1.bind("<Key>", self.HourKeyPress)		

		if HourIndex == 1:
			self.Hour2 = Label(self.parent, text = '   2   ', font=("Courier,22"), background = "green")
		else:
			self.Hour2 = Label(self.parent, text = '   2   ', font=("Courier,22"), background = "white")

		self.Hour2.pack(side = LEFT)
		self.Hour2.bind("<Key>", self.HourKeyPress)		
	
		if HourIndex == 2:
			self.Hour3 = Label(self.parent, text = '   3   ', font=("Courier,22"), background = "green")
		else:
			self.Hour3 = Label(self.parent, text = '   3   ', font=("Courier,22"), background = "white")

		self.Hour3.pack(side = LEFT)
		self.Hour3.bind("<Key>", self.HourKeyPress)		

		if HourIndex == 3:
			self.Hour4 = Label(self.parent, text = '   4   ', font=("Courier,22"), background = "green")
		else:
			self.Hour4 = Label(self.parent, text = '   4   ', font=("Courier,22"), background = "white")

		self.Hour4.pack(side = LEFT)
		self.Hour4.bind("<Key>", self.HourKeyPress)		

		if HourIndex == 4:
			self.Hour5 = Label(self.parent, text = '   5   ', font=("Courier,22"), background = "green")
		else:
			self.Hour5 = Label(self.parent, text = '   5   ', font=("Courier,22"), background = "white")
		
		self.Hour5.pack(side = LEFT)
		self.Hour5.bind("<Key>", self.HourKeyPress)

		if HourIndex == 5:
			self.Hour6 = Label(self.parent, text = '   6   ', font=("Courier,22"), background = "green")
		else:
			self.Hour6 = Label(self.parent, text = '   6   ', font=("Courier,22"), background = "white")

		self.Hour6.pack(side = LEFT)
		self.Hour6.bind("<Key>", self.HourKeyPress)

		if HourIndex == 6:
			self.Hour7 = Label(self.parent, text = '   7   ', font=("Courier,22"), background = "green")
		else:
			self.Hour7 = Label(self.parent, text = '   7   ', font=("Courier,22"), background = "white")

		self.Hour7.pack(side = LEFT)
		self.Hour7.bind("<Key>", self.HourKeyPress)

		if HourIndex == 7:
			self.Hour8 = Label(self.parent, text = '   8   ', font=("Courier,22"), background = "green")
		else:
			self.Hour8 = Label(self.parent, text = '   8   ', font=("Courier,22"), background = "white")

		self.Hour8.pack(side = LEFT)
		self.Hour8.bind("<Key>", self.HourKeyPress)

		if HourIndex == 8:
			self.Hour9 = Label(self.parent, text = '   9   ', font=("Courier,22"), background = "green")
		else:
			self.Hour9 = Label(self.parent, text = '   9   ', font=("Courier,22"), background = "white")

		self.Hour9.pack(side = LEFT)
		self.Hour9.bind("<Key>", self.HourKeyPress)

		if HourIndex == 9:
			self.Hour10 = Label(self.parent, text = '   10   ', font=("Courier,22"), background = "green")
		else:
			self.Hour10 = Label(self.parent, text = '   10   ', font=("Courier,22"), background = "white")

		self.Hour10.pack(side = LEFT)
		self.Hour10.bind("<Key>", self.HourKeyPress)

		if HourIndex == 10:
			self.Hour11 = Label(self.parent, text = '   11   ', font=("Courier,22"), background = "green")
		else:
			self.Hour11 = Label(self.parent, text = '   11   ', font=("Courier,22"), background = "white")

		self.Hour11.pack(side = LEFT)
		self.Hour11.bind("<Key>", self.HourKeyPress)

		if HourIndex == 11:
			self.Hour12 = Label(self.parent, text = '   12   ', font=("Courier,22"), background = "green")
		else:
			self.Hour12 = Label(self.parent, text = '   12   ', font=("Courier,22"), background = "white")

		self.Hour12.pack(side = LEFT)
		self.Hour12.bind("<Key>", self.HourKeyPress)

		if HourIndex == 12:
			self.Hour13 = Label(self.parent, text = '   AM   ', font=("Courier,22"), background ="green")
		else:
			self.Hour13 = Label(self.parent, text = '   AM   ', font=("Courier,22"), background ="white")

		self.Hour13.pack(side = LEFT)
		self.Hour13.bind("<Key>", self.HourKeyPress)

		self.frame.pack()
		self.parent.bind("<Key>", self.HourKeyPress)

	#close the window
	def close_windows(self):
		self.parent.destroy()

	#what happens when j,k, or space is hit in the hour menu
	def HourKeyPress(self,event):
		global HourIndex
		global AMorPM
		if event.keysym == 'space' or event.char == event.keysym:

			if event.char == 'j':
				if HourIndex == 0:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="green")
					if AMorPM == 0:
						Sounds = Sound( "wav_files/hours_f/AM_f.wav")
						Sounds.play()
					else:
						Sounds = Sound( "wav_files/hours_f/PM_f.wav")
						Sounds.play()

					HourIndex = 12

				elif HourIndex == 1:
					self.Hour1.configure(background ="green")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/01_f.wav")
					Sounds.play()
					HourIndex = 0

				elif HourIndex == 2:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="green")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/02_f.wav")
					Sounds.play()
					HourIndex = 1

				elif HourIndex == 3:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="green")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/03_f.wav")
					Sounds.play()
					HourIndex = 2

				elif HourIndex == 4:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="green")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/04_f.wav")
					Sounds.play()
					HourIndex = 3

				elif HourIndex == 5:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="green")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/05_f.wav")
					Sounds.play()
					HourIndex = 4

				elif HourIndex == 6:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="green")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/06_f.wav")
					Sounds.play()
					HourIndex = 5

				elif HourIndex == 7:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="green")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/07_f.wav")
					Sounds.play()
					HourIndex = 6

				elif HourIndex == 8:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="green")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/08_f.wav")
					Sounds.play()
					HourIndex = 7

				elif HourIndex == 9:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="green")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/09_f.wav")
					Sounds.play()
					HourIndex = 8

				elif HourIndex == 10:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="green")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/10_f.wav")
					Sounds.play()
					HourIndex = 9

				elif HourIndex == 11:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="green")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/11_f.wav")
					Sounds.play()
					HourIndex = 10

				elif HourIndex == 12:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="green")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/12_f.wav")
					Sounds.play()
					HourIndex = 11

			elif event.char == 'k':
				if HourIndex == 11:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="green")
					if AMorPM == 0:
						Sounds = Sound( "wav_files/hours_f/AM_f.wav")
						Sounds.play()
					else:
						Sounds = Sound( "wav_files/hours_f/PM_f.wav")
						Sounds.play()

					HourIndex = 12

				elif HourIndex == 12:
					self.Hour1.configure(background ="green")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/01_f.wav")
					Sounds.play()
					HourIndex = 0

				elif HourIndex == 0:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="green")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/02_f.wav")
					Sounds.play()
					HourIndex = 1

				elif HourIndex == 1:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="green")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/03_f.wav")
					Sounds.play()
					HourIndex = 2

				elif HourIndex == 2:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="green")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/04_f.wav")
					Sounds.play()
					HourIndex = 3

				elif HourIndex == 3:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="green")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/05_f.wav")
					Sounds.play()
					HourIndex = 4

				elif HourIndex == 4:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="green")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/06_f.wav")
					Sounds.play()
					HourIndex = 5

				elif HourIndex == 5:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="green")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/07_f.wav")
					Sounds.play()
					HourIndex = 6

				elif HourIndex == 6:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="green")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/08_f.wav")
					Sounds.play()
					HourIndex = 7

				elif HourIndex == 7:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="green")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/09_f.wav")
					Sounds.play()
					HourIndex = 8

				elif HourIndex == 8:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="green")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/10_f.wav")
					Sounds.play()
					HourIndex = 9

				elif HourIndex == 9:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="green")
					self.Hour12.configure(background ="white")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/11_f.wav")
					Sounds.play()
					HourIndex = 10

				elif HourIndex == 10:
					self.Hour1.configure(background ="white")
					self.Hour2.configure(background ="white")
					self.Hour3.configure(background ="white")
					self.Hour4.configure(background ="white")
					self.Hour5.configure(background ="white")
					self.Hour6.configure(background ="white")
					self.Hour7.configure(background ="white")
					self.Hour8.configure(background ="white")
					self.Hour9.configure(background ="white")
					self.Hour10.configure(background ="white")
					self.Hour11.configure(background ="white")
					self.Hour12.configure(background ="green")
					self.Hour13.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/12_f.wav")
					Sounds.play()
					HourIndex = 11

			elif event.keysym == 'space':
				if HourIndex == 12:
					if AMorPM == 0:
						self.Hour13.configure(text = "   PM   ")
						Sounds = Sound( "wav_files/hours_f/PM_f.wav")
						Sounds.play()
						AMorPM = 1
					
					else:
						
						self.Hour13.configure(text = "   AM   ")
						Sounds = Sound( "wav_files/hours_f/AM_f.wav")
						Sounds.play()
						AMorPM = 0
				else:
					self.close_windows()




#the class that handles the minute selection
class Minute:
	def __init__(self,parent):
		self.parent = parent
		self.frame = Frame(parent)

		if MinuteIndex == 0:
			self.Minute1 = Label(self.parent, text = '   0   ', font=("Courier,22"), background = "green")
		else:
			self.Minute1 = Label(self.parent, text = '   0   ', font=("Courier,22"), background = "white")

		self.Minute1.pack(side = LEFT)
		self.Minute1.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 1:
			self.Minute2 = Label(self.parent, text = '   5   ', font=("Courier,22"), background = "green")
		else:
			self.Minute2 = Label(self.parent, text = '   5   ', font=("Courier,22"), background = "white")

		self.Minute2.pack(side = LEFT)
		self.Minute2.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 2:
			self.Minute3 = Label(self.parent, text = '   10   ', font=("Courier,22"), background = "green")
		else:
			self.Minute3 = Label(self.parent, text = '   10   ', font=("Courier,22"), background = "white")

		self.Minute3.pack(side = LEFT)
		self.Minute3.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 3:
			self.Minute4 = Label(self.parent, text = '   15   ', font=("Courier,22"), background = "green")
		else:
			self.Minute4 = Label(self.parent, text = '   15   ', font=("Courier,22"), background = "white")

		self.Minute4.pack(side = LEFT)
		self.Minute4.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 4:
			self.Minute5 = Label(self.parent, text = '   20   ', font=("Courier,22"), background = "green")
		else:
			self.Minute5 = Label(self.parent, text = '   20   ', font=("Courier,22"), background = "white")

		self.Minute5.pack(side = LEFT)
		self.Minute5.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 5:
			self.Minute6 = Label(self.parent, text = '   25   ', font=("Courier,22"), background = "green")
		else:
			self.Minute6 = Label(self.parent, text = '   25   ', font=("Courier,22"), background = "white")

		self.Minute6.pack(side = LEFT)
		self.Minute6.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 6:
			self.Minute7 = Label(self.parent, text = '   30   ', font=("Courier,22"), background = "green")
		else:
			self.Minute7 = Label(self.parent, text = '   30   ', font=("Courier,22"), background = "white")

		self.Minute7.pack(side = LEFT)
		self.Minute7.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 7:
			self.Minute8 = Label(self.parent, text = '   35   ', font=("Courier,22"), background = "green")
		else:
			self.Minute8 = Label(self.parent, text = '   35   ', font=("Courier,22"), background = "white")

		self.Minute8.pack(side = LEFT)
		self.Minute8.bind("<Key>", self.MinuteKeyPress)
		
		if MinuteIndex == 8:
			self.Minute9 = Label(self.parent, text = '   40   ', font=("Courier,22"), background = "green")
		else:
			self.Minute9 = Label(self.parent, text = '   40   ', font=("Courier,22"), background = "white")

		self.Minute9.pack(side = LEFT)
		self.Minute9.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 9:
			self.Minute10 = Label(self.parent, text = '   45   ', font=("Courier,22"), background = "green")
		else:
			self.Minute10 = Label(self.parent, text = '   45   ', font=("Courier,22"), background = "white")

		self.Minute10.pack(side = LEFT)
		self.Minute10.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 10:
			self.Minute11 = Label(self.parent, text = '   50   ', font=("Courier,22"), background = "green")
		else:
			self.Minute11 = Label(self.parent, text = '   50   ', font=("Courier,22"), background = "white")

		self.Minute11.pack(side = LEFT)
		self.Minute11.bind("<Key>", self.MinuteKeyPress)		

		if MinuteIndex == 11:
			self.Minute12 = Label(self.parent, text = '   55   ', font=("Courier,22"), background = "green")
		else:
			self.Minute12 = Label(self.parent, text = '   55   ', font=("Courier,22"), background = "white")

		self.Minute12.pack(side = LEFT)
		self.Minute12.bind("<Key>", self.MinuteKeyPress)		

		self.frame.pack()
		self.parent.bind("<Key>", self.MinuteKeyPress)

	#close the window
	def close_windows(self):
		self.parent.destroy()

	#what happens when you hit j,k or space when in the minutes menu
	def MinuteKeyPress(self,event):
		global MinuteIndex
		if event.keysym == 'space' or event.char == event.keysym:

			if event.char == 'j':

				if MinuteIndex == 0:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="green")
					Sounds = Sound( "wav_files/minutes_f/55_f.wav")
					Sounds.play()
					MinuteIndex = 11

				elif MinuteIndex == 1:
					self.Minute1.configure(background ="green")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/00_f.wav")
					Sounds.play()
					MinuteIndex = 0

				elif MinuteIndex == 2:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="green")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/05_f.wav")
					Sounds.play()
					MinuteIndex = 1

				elif MinuteIndex == 3:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="green")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/10_f.wav")
					Sounds.play()
					MinuteIndex = 2

				elif MinuteIndex == 4:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="green")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/15_f.wav")
					Sounds.play()
					MinuteIndex = 3

				elif MinuteIndex == 5:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="green")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/20_f.wav")
					Sounds.play()
					MinuteIndex = 4

				elif MinuteIndex == 6:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="green")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/25_f.wav")
					Sounds.play()
					MinuteIndex = 5

				elif MinuteIndex == 7:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="green")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/30_f.wav")
					Sounds.play()
					MinuteIndex = 6

				elif MinuteIndex == 8:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="green")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/35_f.wav")
					Sounds.play()
					MinuteIndex = 7

				elif MinuteIndex == 9:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="green")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/40_f.wav")
					Sounds.play()
					MinuteIndex = 8

				elif MinuteIndex == 10:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="green")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/45_f.wav")
					Sounds.play()
					MinuteIndex = 9

				elif MinuteIndex == 11:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="green")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/50_f.wav")
					Sounds.play()
					MinuteIndex = 10


			elif event.char == 'k':

				if MinuteIndex == 11:
					self.Minute1.configure(background ="green")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/00_f.wav")
					Sounds.play()
					MinuteIndex = 0

				elif MinuteIndex == 0:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="green")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/05_f.wav")
					Sounds.play()
					MinuteIndex = 1

				elif MinuteIndex == 1:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="green")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/10_f.wav")
					Sounds.play()
					MinuteIndex = 2

				elif MinuteIndex == 2:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="green")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/15_f.wav")
					Sounds.play()
					MinuteIndex = 3

				elif MinuteIndex == 3:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="green")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/20_f.wav")
					Sounds.play()
					MinuteIndex = 4

				elif MinuteIndex == 4:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="green")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/25_f.wav")
					Sounds.play()
					MinuteIndex = 5

				elif MinuteIndex == 5:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="green")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/30_f.wav")
					Sounds.play()
					MinuteIndex = 6

				elif MinuteIndex == 6:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="green")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/35_f.wav")
					Sounds.play()
					MinuteIndex = 7

				elif MinuteIndex == 7:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="green")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/40_f.wav")
					Sounds.play()
					MinuteIndex = 8

				elif MinuteIndex == 8:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="green")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/45_f.wav")
					Sounds.play()
					MinuteIndex = 9

				elif MinuteIndex == 9:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="green")
					self.Minute12.configure(background ="white")
					Sounds = Sound( "wav_files/minutes_f/50_f.wav")
					Sounds.play()
					MinuteIndex = 10

				elif MinuteIndex == 10:
					self.Minute1.configure(background ="white")
					self.Minute2.configure(background ="white")
					self.Minute3.configure(background ="white")
					self.Minute4.configure(background ="white")
					self.Minute5.configure(background ="white")
					self.Minute6.configure(background ="white")
					self.Minute7.configure(background ="white")
					self.Minute8.configure(background ="white")
					self.Minute9.configure(background ="white")
					self.Minute10.configure(background ="white")
					self.Minute11.configure(background ="white")
					self.Minute12.configure(background ="green")
					Sounds = Sound( "wav_files/minutes_f/55_f.wav")
					Sounds.play()
					MinuteIndex = 11

			elif event.keysym == 'space':
				self.close_windows()




#This is the main class that starts on first execution of the program. this starts the selection menu for
#day,hour,minute or exit
class GUIAPP:
	def __init__(self, parent):
		self.parent = parent
		self.frame = Frame(parent)
		self.frame.pack()
		self.parent.bind("<Key>", self.keyPress)

		self.label1 = Label(self.parent)
		if ColorIndex == 0:
			self.label1.configure(font=("Courier",32),text="   Set day   ", background ="green")
		else:
			self.label1.configure(font=("Courier",32),text="   Set day   ", background ="white")

		self.label1.pack(side=LEFT)
		self.label1.bind("<Key>", self.keyPress)


		self.label2 = Label(self.parent)
		if ColorIndex == 1:
			self.label2.configure(font=("Courier",32),text="   Set hour   ", background ="green")
		else:
			self.label2.configure(font=("Courier",32),text="   Set hour   ", background ="white")

		self.label2.pack(side=LEFT)
		self.label2.bind("<Key>", self.keyPress)
		

		self.label3 = Label(self.parent)
		if ColorIndex == 2:
			self.label3.configure(font=("Courier",32),text="   Set minute   ", background ="green")
		else:
			self.label3.configure(font=("Courier",32),text="   Set minute   ", background ="white")

		self.label3.pack(side=LEFT)
		self.label3.bind("<Key>", self.keyPress)

		self.label4 = Label(self.parent)
		if ColorIndex == 3:
			self.label4.configure(font=("Courier",32),text="   Exit program   ", background ="green")
		else:
			self.label4.configure(font=("Courier",32),text="   Exit program   ", background ="white")

		self.label4.pack(side=LEFT)
		self.label4.bind("<Key>", self.keyPress)

	#open day menu
	def new_window(self):
		self.newWindow = Toplevel(self.parent)
		self.app = Day(self.newWindow)
	
	#open hour menu
	def new_window_Hour(self):
		self.newWindowHour = Toplevel(self.parent)
		self.app = Hour(self.newWindowHour)
	
	#open minute menu
	def new_window_Minute(self):
		self.newWindowMinute = Toplevel(self.parent)
		self.app = Minute(self.newWindowMinute)

	#close main menu
	def close_windows(self):
		self.parent.destroy()

	#what happens when the j,k or space is hit when in the main menu
	def keyPress(self,event):
		global ColorIndex
		if event.keysym == 'space' or event.char == event.keysym:
			if event.char == 'k':
				if ColorIndex == 0:
					self.label1.configure(background ="white")
					self.label2.configure(background ="green")
					self.label3.configure(background ="white")
					self.label4.configure(background ="white")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/Set_hour_f.wav")
					Sounds.play()
					ColorIndex = 1

				elif ColorIndex == 1:
					self.label1.configure(background ="white")
					self.label2.configure(background ="white")
					self.label3.configure(background ="green")
					self.label4.configure(background ="white")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/Set_minutes_f.wav")
					Sounds.play()
					ColorIndex = 2

				elif ColorIndex == 2:
					self.label1.configure(background ="white")
					self.label2.configure(background ="white")
					self.label3.configure(background ="white")
					self.label4.configure(background ="green")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/exit_f.wav")
					Sounds.play()
					ColorIndex = 3

				elif ColorIndex == 3:
					self.label1.configure(background ="green")
					self.label2.configure(background ="white")
					self.label3.configure(background ="white")
					self.label4.configure(background ="white")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/Set_day_of_week_f.wav")
					Sounds.play()
					ColorIndex = 0

			elif event.char == 'j':
				if ColorIndex == 0:
					self.label1.configure(background ="white")
					self.label2.configure(background ="white")
					self.label3.configure(background ="white")
					self.label4.configure(background ="green")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/exit_f.wav")
					Sounds.play()
					ColorIndex = 3

				elif ColorIndex == 1:
					self.label1.configure(background ="green")
					self.label2.configure(background ="white")
					self.label3.configure(background ="white")
					self.label4.configure(background ="white")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/Set_day_of_week_f.wav")
					Sounds.play()
					ColorIndex = 0

				elif ColorIndex == 2:
					self.label1.configure(background ="white")
					self.label2.configure(background ="green")
					self.label3.configure(background ="white")
					self.label4.configure(background ="white")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/Set_hour_f.wav")
					Sounds.play()
					ColorIndex = 1

				elif ColorIndex == 3:
					self.label1.configure(background ="white")
					self.label2.configure(background ="white")
					self.label3.configure(background ="green")
					self.label4.configure(background ="white")
					Sounds = Sound( "wav_files/menus_modes_navigation_f/Set_minutes_f.wav")
					Sounds.play()
					ColorIndex = 2

			elif event.keysym == 'space':

				if ColorIndex == 0:
		
					self.new_window()

				elif ColorIndex == 1:
					
					self.new_window_Hour()

				elif ColorIndex == 2:

					self.new_window_Minute()
				
				elif ColorIndex == 3:
					
					self.close_windows()


root = Tk()
GUIAPP = GUIAPP(root)
root.mainloop()

