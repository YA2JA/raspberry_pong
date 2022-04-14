######################################
# IMPORTATION DES DIFFERENTS MODULES #
######################################
# Modules Natifs
import board
import digitalio
import analogio

class gestion_controles() :

    def __init__(self,joy_x=board.GP26, joy_y=board.GP27, joy_bp=board.GP22, bph=board.GP6, bpb=board.GP7, bpg=board.GP8, bpd=board.GP9) :
        # Joysticks analogiques 2 axes
        self.joystick_Y = analogio.AnalogIn(joy_y)
        self.joystick_X = analogio.AnalogIn(joy_x)
		
        # Bouton du joystick
        self.bouton_JOYSTICK = digitalio.DigitalInOut(joy_bp)
        self.bouton_JOYSTICK.direction = digitalio.Direction.INPUT
        self.bouton_JOYSTICK.pull = digitalio.Pull.UP

        # Bouton haut
        self.bouton_H = digitalio.DigitalInOut(bph)
        self.bouton_H.direction = digitalio.Direction.INPUT
        self.bouton_H.pull = digitalio.Pull.UP
        # Bouton bas
        self.bouton_B = digitalio.DigitalInOut(bpb)
        self.bouton_B.direction = digitalio.Direction.INPUT
        self.bouton_B.pull = digitalio.Pull.UP
        # Bouton droit
        self.bouton_D = digitalio.DigitalInOut(bpd)
        self.bouton_D.direction = digitalio.Direction.INPUT
        self.bouton_D.pull = digitalio.Pull.UP
        # Bouton gauche
        self.bouton_G = digitalio.DigitalInOut(bpg)
        self.bouton_G.direction = digitalio.Direction.INPUT
        self.bouton_G.pull = digitalio.Pull.UP

