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
    {"note" : 41, "on_color" : GREEN, "off_color" : OFF}, 
    {"note" : 42, "on_color" : GREEN, "off_color" : OFF}, 
    {"note" : 43, "on_color" : GREEN, "off_color" : OFF}] 

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
