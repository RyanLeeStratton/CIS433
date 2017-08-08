__author__ = 'Ryan Stratton'

########################################################################################################################
#set_clock.py
#Ryan Stratton
#Fall2016
#build using the sample code provided by the professor.
#initial design for the first assignment of the User interface at UofO
#incomplete version, needs better control design
########################################################################################################################

# Package imports
import readchar

from audioArray import *

#clock audio controls
CYCLE_UP    = 'j'
CYCLE_DOWN  = 'k'

SET         = 'l'
BACK        = ';'
EXIT        = ' '


#what state the system is in for setting the audio for the clock
state = 0

#place holders for array indexes
dayPosition     = 0
hourPosition    = 0
minutePosition  = 0
hourSelection   = 1

########################################################################################################################
#state 0 is for setting the day, 1 for the hour and 2 for the minute.
#the controls currently allow for scrolling foward/backward through each state using the same buttons.
########################################################################################################################


#endless loop to dectect user input and respond
#currently doesn't use the EXIT key to end the loop (I havn't copied the code from the sample yet)
playInfo[0].play_to_end()

while True:

    inputCharacter = readchar.readchar()

    #set day
    if state == 0:
        if inputCharacter == CYCLE_UP:
            dayPosition = (dayPosition + 1)%7
            playDay[dayPosition].play()


        elif inputCharacter == CYCLE_DOWN:
            dayPosition = (dayPosition - 1) % 7
            playDay[dayPosition].play()


        elif inputCharacter == SET:
            state = 1
            playInfo[2].play()
            #goes to set hour menu


        elif inputCharacter == BACK:
            state = 0
            playInfo[1].play()
            #doesn't do anything, audio plays for understanding



        elif inputCharacter == EXIT:
            state = 0
            playInfo[5].play_to_end()
            #exiting progam audio
            break

    #end day selection

    #set hour
    elif state == 1:
        if inputCharacter == CYCLE_UP:
            hourPosition = (hourPosition + 1) % 24
            hourSelection = (hourSelection +1) % 12
            playHour[hourPosition].play()

        if inputCharacter == CYCLE_DOWN:
            hourPosition = (hourPosition - 1) % 24
            hourSelection = (hourSelection - 1) % 12
            playHour[hourPosition].play()

        if inputCharacter == SET:
            state = 2
            playInfo[3].play()

        if inputCharacter == BACK:
            state = 0
            playInfo[1].play()
            # audio about going back to day selection

        if inputCharacter == EXIT:
            state = 1
            playInfo[5].play_to_end()
            # exiting progam audio
            break

    # end hour selection

    #set minute
    elif state == 2:
        if inputCharacter == CYCLE_UP:
            minutePosition = (minutePosition + 1) % 60
            playMinutes[minutePosition].play()

        if inputCharacter == CYCLE_DOWN:
            minutePosition = (minutePosition - 1) % 60
            playMinutes[minutePosition].play()

        if inputCharacter == SET:
            state = 4
            playInfo[6].play_to_end()
            playDay[dayPosition].play_to_end()

            #play the 12 sound
            if hourSelection == 0:
                playMinutes[12].play_to_end()

            else:
                playMinutes[hourSelection].play_to_end()

            #play o clock sound
            if minutePosition == 0:
                playInfo[9].play_to_end()

            else:
                playMinutes[minutePosition].play_to_end()
            #play AM
            if hourPosition <= 10:
                playInfo[7].play_to_end()

            elif hourPosition == 23:
                playInfo[7].play_to_end()

            #play PM
            else:
                playInfo[8].play_to_end()
            break
            #audio selection being finished

        if inputCharacter == BACK:
            state = 1
            playInfo[2].play()
            # audio about going back to hour selection, remove state = 1 when audio added

        if inputCharacter == EXIT:
            state = 2
            playInfo[5].play_to_end()
            # exiting progam audio
            break

    # end minute selection

