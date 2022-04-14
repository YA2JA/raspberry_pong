######################################
# IMPORTATION DES DIFFERENTS MODULES #
######################################
# Modules Natifs
import board
import displayio
import busio
import terminalio
import vectorio
# Modules extérieurs
from adafruit_st7735r import ST7735R
import adafruit_imageload
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

class pong() :

    def __init__(self,mosi_lcd=board.GP11, miso_lcd=board.GP12, sck_lcd=board.GP10, cs_lcd=board.GP13, dc_lcd=board.GP15, res_lcd=board.GP14) :
        # libère toute ressource précédemment utilisée pour un écran
        displayio.release_displays()
        # instanciation du bus SPI pour l'écran
        self.spi_lcd = busio.SPI(MOSI=mosi_lcd, MISO=miso_lcd, clock=sck_lcd)
        self.bus_affichage = displayio.FourWire(self.spi_lcd, command=dc_lcd, chip_select=cs_lcd, reset=res_lcd)
        # instanciation de l'écran
        self.ecran = ST7735R(self.bus_affichage, width=160, height=128, colstart=2, rowstart=1, rotation=90, bgr=True)
        self.largeur_ecran = 159
        self.hauteur_ecran = 127

        # instanciation du groupe d'affichage
        self.groupe_elements = displayio.Group()

        # Ressource titre : fond
        fichier_fond = open("images/pong/Fond_titre.bmp", 'rb')
        image_bmp = displayio.OnDiskBitmap(fichier_fond)
        self.fond = displayio.TileGrid(image_bmp, pixel_shader=displayio.ColorConverter())

        # Ressource titre : joueuse_tennis
        joueuse_sheet, palette_joueuse = adafruit_imageload.load("images/pong/Joueuse_tennis.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
        palette_joueuse.make_transparent(0)
        self.joueuse = displayio.TileGrid(joueuse_sheet,pixel_shader=palette_joueuse, x=15, y=0)

        # Ressource titre : label 'star'
        self.message_start = label.Label(terminalio.FONT, text="< START >", color=0xFFFFFF, x=60, y=110)

        # Ressource jeu : fond
        fichier_fond_jeu = open("images/pong/Fond_jeu.bmp", 'rb')
        terrain_bmp = displayio.OnDiskBitmap(fichier_fond_jeu)
        self.terrain = displayio.TileGrid(terrain_bmp, pixel_shader=displayio.ColorConverter())

        # Ajout d'une police personnalisée
        police_28 = bitmap_font.load_font("fonts/LettersforLearners-28.bdf")

        # Ressource jeu : label 'message'
        self.message = label.Label(font=police_28, text="  Prêts...\nPartie en\n10 points", color=0xFFFFFF, x=42, y=37, scale=1, line_spacing=0.8)

        # Ressource jeu : raquettes
        palette_raquette = displayio.Palette(1)
        palette_raquette[0] = 0xDDDDDD
        self.largeur_raquette = 6
        self.hauteur_raquette = 25
        self.raquette_G = vectorio.Rectangle(pixel_shader=palette_raquette, width=self.largeur_raquette, height=self.hauteur_raquette, x=0, y=50)
        self.raquette_D = vectorio.Rectangle(pixel_shader=palette_raquette, width=self.largeur_raquette, height=self.hauteur_raquette, x=self.largeur_ecran-self.largeur_raquette, y=50)

        # Ressource jeu : balle bitmap
        balle_bmp_sheet, palette_balle_bmp = adafruit_imageload.load("images/pong/Balle_tennis.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
        palette_balle_bmp.make_transparent(0)
        self.balle_bmp = displayio.TileGrid(balle_bmp_sheet,pixel_shader=palette_balle_bmp, width=1, height=1, x=74, y=10)
        self.diametre_balle = 12

        # Ressource jeu : balle vectorielle
        palette_balle = displayio.Palette(1)
        palette_balle[0] = 0xDDDDDD
        self.balle = vectorio.Circle(pixel_shader=palette_balle, radius=6, x=80, y=20)

        # Ajout d'une police personnalisée
        police_72 = bitmap_font.load_font("fonts/Boogaloo-Regular-72.bdf")

        # Ressource jeu : labels des scores
        self.score_G = label.Label(font=police_72, text="0", color=0xFFFFFF, x=25, y=55, scale=1)
        self.score_D = label.Label(font=police_72, text="0", color=0xFFFFFF, x=100, y=55, scale=1)

        # Ressource fin: fond
        fichier_fond_gagnant = open("images/pong/Image_gagnant.bmp", 'rb')
        gagnant_bmp = displayio.OnDiskBitmap(fichier_fond_gagnant)
        self.fond_gagnant = displayio.TileGrid(gagnant_bmp, pixel_shader=displayio.ColorConverter())

        # Ressource fin : label 'vainqueur'
        self.vainqueur = label.Label(font=police_28, text="Joueur x", color=0xFFFFFF, x=70, y=50)

        # Affiche une étoile
#         etoile_sheet, palette_etoile = adafruit_imageload.load("images/Tutoriel/Sparkle.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
#         palette_etoile.make_transparent(0)
#         self.etoile = displayio.TileGrid(etoile_sheet,pixel_shader=palette_etoile, width=1, height=1, tile_width=16, tile_height=16, default_tile=0 , x=55, y=65)


