######################################
# Modules Natifs
import time
from random import randint

# Modules du dossier 'lib'
import Ressources_pong
import Gestion_controles
import Gestion_audio

######################################
#  INSTANCIATION DES OBJETS UTILES   #
######################################

# Création d'un objet donnant accès aux contrôles (joystick et boutons)
controles = Gestion_controles.gestion_controles()

# Création d'un objet donnant accès au contrôle de l'audio
lecteur_mp3 = Gestion_audio.gestion_audio()

# Création d'un objet 'ressources' contenant les éléments graphiques
ressources = Ressources_pong.pong()
pause_exit = 0
balle_speed = (1, 0)
controlle_speed = 2
speed = 0.02
board_down_limit = 127-ressources.hauteur_raquette
raquette_centre = (ressources.hauteur_raquette/2)

#########################
#  ECRAN DE DEMARRAGE   #
#########################
for i in range(len(ressources.groupe_elements)):
        ressources.groupe_elements.pop(-1)

ressources.groupe_elements.append(ressources.fond)
ressources.groupe_elements.append(ressources.joueuse)
ressources.groupe_elements.append(ressources.message_start)
ressources.ecran.show(ressources.groupe_elements)

def start_game():
    for i in range(len(ressources.groupe_elements)):
        ressources.groupe_elements.pop(-1)

    ressources.groupe_elements.append(ressources.terrain)
    ressources.groupe_elements.append(ressources.raquette_G)
    ressources.groupe_elements.append(ressources.raquette_D)
    ressources.groupe_elements.append(ressources.balle)
    ressources.balle.x = int(159/2)
    ressources.balle.y = int(127/2)

def jeu():
    global balle_speed, speed

    #mvt balle
    ressources.balle.x += balle_speed[0]
    ressources.balle.y += balle_speed[1]

    if (ressources.balle.x > 155) or (ressources.balle.x < 0):
        speed = 0.02
        if  (ressources.balle.x > 155):
            ressources.score_G.text = str(int(ressources.score_G.text )+1)

        if  (ressources.balle.x < 0):
            ressources.score_D.text = str(int(ressources.score_D.text )+1)

        ressources.balle.x = int(159/2)
        ressources.balle.y = int(127/2)
        ball_speed = (0, 0)
        ressources.groupe_elements.append(ressources.score_D)
        ressources.groupe_elements.append(ressources.score_G)
        time.sleep(1)

        ressources.groupe_elements.pop(ressources.groupe_elements.index(ressources.score_D))
        ressources.groupe_elements.pop(ressources.groupe_elements.index(ressources.score_G))

        while balle_speed[0] == 0:
            balle_speed = (randint(-1,1), randint(-1,1))

    if (
        (ressources.balle.y <= ressources.raquette_D.y+ressources.hauteur_raquette) and
        (ressources.balle.y >= ressources.raquette_D.y) and
        (ressources.balle.x >= ressources.largeur_ecran-ressources.largeur_raquette)
        ) or (
        (ressources.balle.y <= ressources.raquette_G.y+ressources.hauteur_raquette) and
        (ressources.balle.y >= ressources.raquette_G.y) and
        (ressources.balle.x <= ressources.largeur_raquette)):

            speed -=0.0005 if speed >= 0.0007 else 0.000001

            if (ressources.balle.x-80 < 0):
                vec_y = int(((ressources.balle.y-(ressources.raquette_G.y+raquette_centre))/10)*3)
            else:
                vec_y = int(((ressources.balle.y-(ressources.raquette_D.y+raquette_centre)) /10)*3)

            balle_speed = (-balle_speed[0], vec_y)

    if (ressources.balle.y > 127) or (ressources.balle.y < 0):
        balle_speed = (balle_speed[0], -balle_speed[1])

def controllers():
    if controles.joystick_Y.value != 0:
        valeur = (controles.joystick_Y.value>15000)-(controles.joystick_Y.value < 50_000)
        ressources.raquette_D.y -= valeur*controlle_speed
        if ressources.raquette_D.y < 0:
            ressources.raquette_D.y = 0
        elif ressources.raquette_D.y > board_down_limit:
            ressources.raquette_D.y = board_down_limit

    if controles.bouton_H.value == False :
        ressources.raquette_G.y -= controlle_speed
        if ressources.raquette_G.y < 0:
            ressources.raquette_G.y = 0

    elif controles.bouton_B.value == False :
        ressources.raquette_G.y += controlle_speed
        if ressources.raquette_G.y > board_down_limit:
            ressources.raquette_G.y = board_down_limit

####################
####################
#  BOUCLE INFINIE  #
####################
####################

while True:
    pause_exit = (pause_exit+1) %50
    if pause_exit == 49:
        ressources.message_start.color = 0xFFFFFF
        time.sleep(0.15)
        ressources.message_start.color = 0x000000
        time.sleep(0.15)

    if not controles.bouton_JOYSTICK.value:
        ###############################
        #  PREPARATION DE LA PARTIE   #
        ###############################
        start_game()

        ##########################
        #  PARTIE EN 10 POINTS   #
        ##########################
        while int(ressources.score_D.text) < 10 and int(ressources.score_G.text) < 10:
            controllers()
            jeu()
            time.sleep(speed)

        ressources.groupe_elements.pop(ressources.groupe_elements.index(ressources.balle))
        ressources.groupe_elements.pop(ressources.groupe_elements.index(ressources.raquette_G))
        ressources.groupe_elements.pop(ressources.groupe_elements.index(ressources.raquette_D))
        ressources.groupe_elements.pop(ressources.groupe_elements.index(ressources.terrain))
        ressources.groupe_elements.append(ressources.fond_gagnant)
        ressources.vainqueur.text =  f"Joueur {'\ngauche' if int(ressources.score_G.text) >= 2 else '\ndroit' }"
        ressources.vainqueur.x =  60
        ressources.vainqueur.color = 0xFBC10D
        ressources.groupe_elements.append(ressources.vainqueur)



    ####################
    #  FIN DE PARTIE   #
    ####################
