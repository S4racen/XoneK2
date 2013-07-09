import Live

from Constants import *

from _Allen_And_Heath_Framework.AllenAndHeathMixerComponent import AllenAndHeathMixerComponent
from _Allen_And_Heath_Framework.AllenAndHeathSessionComponent import AllenAndHeathSessionComponent
from _Allen_And_Heath_Framework.AllenAndHeathTransportComponent import AllenAndHeathTransportComponent
from _Allen_And_Heath_Framework.AllenAndHeathSessionZoomingComponent import AllenAndHeathSessionZoomingComponent
from _Allen_And_Heath_Framework.AllenAndHeathControlSurface import AllenAndHeathControlSurface
from _Allen_And_Heath_Framework.LEDButtonElement import LEDButtonElement


class K2(AllenAndHeathControlSurface):
  __module__ = __name__
  __doc__ = " K2 controller script "

  def __init__(self, c_instance):
    AllenAndHeathControlSurface.__init__(self, c_instance)

  def setup_mixer(self):
    self.mixer = AllenAndHeathMixerComponent(
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
    self.session = AllenAndHeathSessionComponent(
        button_class = LEDButtonElement,
        scroll_navigation = SCROLLING,
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
    
