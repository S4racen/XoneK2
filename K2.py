import Live

from Constants import *

from _Livid_Framework.LividMixerComponent import LividMixerComponent
from _Livid_Framework.LividSessionComponent import LividSessionComponent
from _Livid_Framework.LividTransportComponent import LividTransportComponent
from _Livid_Framework.LividSessionZoomingComponent import LividSessionZoomingComponent
from _Livid_Framework.LividControlSurface import LividControlSurface
from _Livid_Framework.LEDButtonElement import LEDButtonElement


class K2(LividControlSurface):
  __module__ = __name__
  __doc__ = " Ohmicide controller script "

  def __init__(self, c_instance):
    LividControlSurface.__init__(self, c_instance)

  def setup_mixer(self):
    self.mixer = LividMixerComponent(
        channel = CHANNEL,
        faders = FADERS, 
        sends = SENDS, 
        color_mappings = COLOR_MAPPINGS,
        button_class = LEDButtonElement, 
        solos = SOLOS)
        #selects = TRACK_SELECTS, 
        #master_select = MASTER_SELECT, 
        #arms = ARMS)
  
  def setup_session(self):
    self.session = LividSessionComponent(
        button_class = LEDButtonElement,
        channel = CHANNEL,
        matrix = MATRIX, 
        color_mappings = COLOR_MAPPINGS,
        triggered_to_play_value = TRIGGERED_VALUE,
        record_value = RECORD_VALUE,
        stopped_value = STOPPED_VALUE,
        started_value = PLAYING_VALUE,
        mixer = self.mixer)
    #self.session_zoom = LividSessionZoomingComponent(self.session, SHIFT)
    
    # Session zoom

  def setup_transport(self):
    pass
    
