######################################
# IMPORTATION DES DIFFERENTS MODULES #
######################################
# Modules Natifs
import board
import digitalio
import busio
# Modules extérieurs
from DFPlayer import DFPlayer

class gestion_audio() :

    def __init__(self,tx_dfplayer=board.GP16, rx_dfplayer=board.GP17, mute=board.GP21, busy=board.GP18) :
        # instanciation du bus UART pour le DFPLayer Mini
        bus_audio = busio.UART(tx=tx_dfplayer, rx=rx_dfplayer, baudrate=9600)
        # instanciation du module DFPlayer
        PLAYER_VOL   = 80
        self.dfplayer_mini = DFPlayer(uart=bus_audio, volume=PLAYER_VOL)
        # Instanciation de la broche AUDIO_BUSY
        self.audio_busy = digitalio.DigitalInOut(busy)
        self.audio_busy.direction = digitalio.Direction.INPUT
        # Instanciation de la broche AUDIO_MUTE
        self.audio_mute = digitalio.DigitalInOut(mute)
        self.audio_mute.direction = digitalio.Direction.OUTPUT
        self.audio_mute.value = True

