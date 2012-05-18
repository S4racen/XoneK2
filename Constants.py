from _Livid_Framework.LividConstants import *

MIDI_CC_TYPE = 1
MIDI_NOTE_TYPE = 0

RETURNS = 0
CHANNEL = 14 # All things must be on one channel

BPM_UP = 61
BPM_DOWN = 62

# It is assumed that these will use the global channel
# And will be CCs
FADERS = [16, 17, 18, 19] 

SENDS = [
  [4, 8, 12], # Channel 1
  [5, 9, 13], # Channel 2 etc
  [6, 10, 14],
  [7, 11, 15]]

SOLOS = [
    {"note" : 40, "on_color" : GREEN, "off_color" : OFF}, 
    41, 42, 43]


NAVIGATION_BUTTONS = {
    'up' : 70,
    'down' : 78,
    'left' : 77,
    'right' : 79}
# Grid of button notes

TRIGGERED_VALUE = RED
RECORD_VALUE = RED
STOPPED_VALUE = YELLOW
PLAYING_VALUE = GREEN

COLOR_MAPPINGS = { # Relative to the root note of the button, not absolute
  RED : 0,
  YELLOW : 36,
  GREEN : 72}

MATRIX = [
    [36, 37,  38, 39],
    [32, 33, 34, 35],
    [28, 29, 30, 31],
    [24, 25, 26, 27]]

SCENE_LAUNCH = [56, 57, 58, 59, 60]

STOPS = [5, 13, 21, 29, 37, 45, 53]

ARMS =  [7, 15, 23, 31, 39, 47, 55]
TRACK_SELECTS =  [65, 73, 66, 74, 67, 75, 68]
MASTER_SELECT = 76
