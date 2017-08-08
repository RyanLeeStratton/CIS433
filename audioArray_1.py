########################################################################################################################
#audioArray.py
#Ryan Stratton
#Fall 2016
#program that sets up the links to audio files.
########################################################################################################################
__author__ = 'Ryan Stratton'

from sound import Sound

#sets the array size for each of the three arrays to hold sound file locations
playDay = [1]*7
playHour = [1]*24
playMinutes = [1]*60
playInfo    = [1]*10

#this section is where the audio for general information is stored
playInfo[0] = Sound \
(   "wav_files/menus_modes_navigation_f/Set_date_and_time_f.wav")
playInfo[1] = Sound \
(   "wav_files/menus_modes_navigation_f/Set_day_of_week_f.wav")
playInfo[2] = Sound \
(   "wav_files/menus_modes_navigation_f/Set_hour_f.wav")
playInfo[3] = Sound \
(   "wav_files/menus_modes_navigation_f/Set_minutes_f.wav")
playInfo[4] = Sound \
(   "wav_files/menus_modes_navigation_f/Press_again_to_quit_f.wav")
playInfo[5] = Sound \
(   "wav_files/menus_modes_navigation_f/exiting_program_f.wav")
playInfo[6] = Sound \
(   "wav_files/menus_modes_navigation_f/you_selected_f.wav")
playInfo[7] = Sound \
(   "wav_files/hours_f/AM_f.wav")
playInfo[8] = Sound \
(   "wav_files/hours_f/PM_f.wav")
playInfo[9] = Sound \
(   "wav_files/menus_modes_navigation_f/o_clock_f.wav")

#this section is where the audio for the days of the week is stored
playDay[0] = Sound \
(   "wav_files/days_of_week_f/friday_f.wav")
playDay[1] = Sound \
    ("wav_files/days_of_week_f/saturday_f.wav")
playDay[2] = Sound \
    ("wav_files/days_of_week_f/sunday_f.wav")
playDay[3] = Sound \
    ("wav_files/days_of_week_f/monday_f.wav")
playDay[4] = Sound \
    ("wav_files/days_of_week_f/tuesday_f.wav")
playDay[5] = Sound \
    ("wav_files/days_of_week_f/wednesday_f.wav")
playDay[6] = Sound \
    ("wav_files/days_of_week_f/thursday_f.wav")

#this section is where the audio for the hours is stored
playHour[0] = Sound \
    ("wav_files/hours_f/.1AM_f.wav")
playHour[1] = Sound \
    ("wav_files/hours_f/.2AM_f.wav")
playHour[2] = Sound \
    ("wav_files/hours_f/.3AM_f.wav")
playHour[3] = Sound \
    ("wav_files/hours_f/.4AM_f.wav")
playHour[4] = Sound \
    ("wav_files/hours_f/.5AM_f.wav")
playHour[5] = Sound \
    ("wav_files/hours_f/.6AM_f.wav")
playHour[6] = Sound \
    ("wav_files/hours_f/.7AM_f.wav")
playHour[7] = Sound \
    ("wav_files/hours_f/.8AM_f.wav")
playHour[8] = Sound \
    ("wav_files/hours_f/.9AM_f.wav")
playHour[9] = Sound \
    ("wav_files/hours_f/.10AM_f.wav")
playHour[10] = Sound \
    ("wav_files/hours_f/.11AM_f.wav")
playHour[11] = Sound \
    ("wav_files/hours_f/.12PM_f.wav")
playHour[12] = Sound \
    ("wav_files/hours_f/1PM_f.wav")
playHour[13] = Sound \
    ("wav_files/hours_f/2PM_f.wav")
playHour[14] = Sound \
    ("wav_files/hours_f/3PM_f.wav")
playHour[15] = Sound \
    ("wav_files/hours_f/4PM_f.wav")
playHour[16] = Sound \
    ("wav_files/hours_f/5PM_f.wav")
playHour[17] = Sound \
    ("wav_files/hours_f/6PM_f.wav")
playHour[18] = Sound \
    ("wav_files/hours_f/7PM_f.wav")
playHour[19] = Sound \
    ("wav_files/hours_f/8PM_f.wav")
playHour[20] = Sound \
    ("wav_files/hours_f/9PM_f.wav")
playHour[21] = Sound \
    ("wav_files/hours_f/10PM_f.wav")
playHour[22] = Sound \
    ("wav_files/hours_f/11PM_f.wav")
playHour[23] = Sound \
    ("wav_files/hours_f/12AM_f.wav")

#this section will is where the audio for mintues is stored

playMinutes[0] = Sound \
    ("wav_files/minutes_f/00_f.wav")
playMinutes[1] = Sound \
    ("wav_files/minutes_f/01_f.wav")
playMinutes[2] = Sound \
    ("wav_files/minutes_f/02_f.wav")
playMinutes[3] = Sound \
    ("wav_files/minutes_f/03_f.wav")
playMinutes[4] = Sound \
    ("wav_files/minutes_f/04_f.wav")
playMinutes[5] = Sound \
    ("wav_files/minutes_f/05_f.wav")
playMinutes[6] = Sound \
    ("wav_files/minutes_f/06_f.wav")
playMinutes[7] = Sound \
    ("wav_files/minutes_f/07_f.wav")
playMinutes[8] = Sound \
    ("wav_files/minutes_f/08_f.wav")
playMinutes[9] = Sound \
    ("wav_files/minutes_f/09_f.wav")
playMinutes[10] = Sound \
    ("wav_files/minutes_f/10_f.wav")
playMinutes[11] = Sound \
    ("wav_files/minutes_f/11_f.wav")
playMinutes[12] = Sound \
    ("wav_files/minutes_f/12_f.wav")
playMinutes[13] = Sound \
    ("wav_files/minutes_f/13_f.wav")
playMinutes[14] = Sound \
    ("wav_files/minutes_f/14_f.wav")
playMinutes[15] = Sound \
    ("wav_files/minutes_f/15_f.wav")
playMinutes[16] = Sound \
    ("wav_files/minutes_f/16_f.wav")
playMinutes[17] = Sound \
    ("wav_files/minutes_f/17_f.wav")
playMinutes[18] = Sound \
    ("wav_files/minutes_f/18_f.wav")
playMinutes[19] = Sound \
    ("wav_files/minutes_f/19_f.wav")
playMinutes[20] = Sound \
    ("wav_files/minutes_f/20_f.wav")
playMinutes[21] = Sound \
    ("wav_files/minutes_f/21_f.wav")
playMinutes[22] = Sound \
    ("wav_files/minutes_f/22_f.wav")
playMinutes[23] = Sound \
    ("wav_files/minutes_f/23_f.wav")
playMinutes[24] = Sound \
    ("wav_files/minutes_f/24_f.wav")
playMinutes[25] = Sound \
    ("wav_files/minutes_f/25_f.wav")
playMinutes[26] = Sound \
    ("wav_files/minutes_f/26_f.wav")
playMinutes[27] = Sound \
    ("wav_files/minutes_f/27_f.wav")
playMinutes[28] = Sound \
    ("wav_files/minutes_f/28_f.wav")
playMinutes[29] = Sound \
    ("wav_files/minutes_f/29_f.wav")
playMinutes[30] = Sound \
    ("wav_files/minutes_f/30_f.wav")
playMinutes[31] = Sound \
    ("wav_files/minutes_f/31_f.wav")
playMinutes[32] = Sound \
    ("wav_files/minutes_f/32_f.wav")
playMinutes[33] = Sound \
    ("wav_files/minutes_f/33_f.wav")
playMinutes[34] = Sound \
    ("wav_files/minutes_f/34_f.wav")
playMinutes[35] = Sound \
    ("wav_files/minutes_f/35_f.wav")
playMinutes[36] = Sound \
    ("wav_files/minutes_f/36_f.wav")
playMinutes[37] = Sound \
    ("wav_files/minutes_f/37_f.wav")
playMinutes[38] = Sound \
    ("wav_files/minutes_f/38_f.wav")
playMinutes[39] = Sound \
    ("wav_files/minutes_f/39_f.wav")
playMinutes[40] = Sound \
    ("wav_files/minutes_f/40_f.wav")
playMinutes[41] = Sound \
    ("wav_files/minutes_f/41_f.wav")
playMinutes[42] = Sound \
    ("wav_files/minutes_f/42_f.wav")
playMinutes[43] = Sound \
    ("wav_files/minutes_f/43_f.wav")
playMinutes[44] = Sound \
    ("wav_files/minutes_f/44_f.wav")
playMinutes[45] = Sound \
    ("wav_files/minutes_f/45_f.wav")
playMinutes[46] = Sound \
    ("wav_files/minutes_f/46_f.wav")
playMinutes[47] = Sound \
    ("wav_files/minutes_f/47_f.wav")
playMinutes[48] = Sound \
    ("wav_files/minutes_f/48_f.wav")
playMinutes[49] = Sound \
    ("wav_files/minutes_f/49_f.wav")
playMinutes[50] = Sound \
    ("wav_files/minutes_f/50_f.wav")
playMinutes[51] = Sound \
    ("wav_files/minutes_f/51_f.wav")
playMinutes[52] = Sound \
    ("wav_files/minutes_f/52_f.wav")
playMinutes[53] = Sound \
    ("wav_files/minutes_f/53_f.wav")
playMinutes[54] = Sound \
    ("wav_files/minutes_f/54_f.wav")
playMinutes[55] = Sound \
    ("wav_files/minutes_f/55_f.wav")
playMinutes[56] = Sound \
    ("wav_files/minutes_f/56_f.wav")
playMinutes[57] = Sound \
    ("wav_files/minutes_f/57_f.wav")
playMinutes[58] = Sound \
    ("wav_files/minutes_f/58_f.wav")
playMinutes[59] = Sound \
    ("wav_files/minutes_f/59_f.wav")
