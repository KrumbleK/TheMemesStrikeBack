import pygame
import sys
import random
from pygame.locals import *

# Alustaa pygamen

pygame.init()
pygame.font.init()
koko = (1000,1000)
ruutu = pygame.display.set_mode(koko)
pygame.display.set_caption("da memes strike back -peli")

ajastin = pygame.time.Clock()
FPS = 30


fontti = pygame.font.SysFont("Ebrima", 30)
tekstivari = (255,255,255)

pelaaja = pygame.image.load("dababycar.png")
lasi = pygame.image.load("vihollinen.png")
tausta = pygame.image.load("tausta.png")
pelaaja = pygame.transform.scale(pelaaja, (95,120))
lasi = pygame.transform.scale(lasi, (95,120))
tausta = pygame.transform.scale(tausta, (1000,1000))
pygame.mixer.music.load("DONUT.mp3")
pygame.mixer.music.play(-1)

pelx = 170
pely = 450
nopeus = 5
vihunopeus = 7
hp = 10
vihut = [[100,100],[400,300],[300,0],[100,300], [100,500], [350,500]]

# Käsittelee tapahtumia
def peruna():
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Pelilogiikka
def porkkana():
    # Taustan piirto
    global pelx
    global pely, hp
    ruutu.blit(tausta, (0,0))

    # Pelaajan liikkuminen
    nappaimet = pygame.key.get_pressed()
    if nappaimet[pygame.K_RIGHT]:
        pelx += nopeus
    if nappaimet[pygame.K_LEFT]:
        pelx -= nopeus
    
    if pelx < 40:
        pelx = 40
    if pelx > 1000:
        pelx = 1000

    # Vihollisten liikkuminen
    for vihu in vihut:
        vihu[1] += vihunopeus
        if vihu[1] > 600:
            vihu[1] = -10
            vihu[0] = random.randint(50, 1000)

    # Vihollisten piirto
    for vihu in vihut:
        ruutu.blit(lasi,vihu)
    
    for vihu in vihut:
         if vihu[1] + 32 > pely and vihu[1] < pely + 64:
             if vihu[0] + 32 > pelx and vihu[0] < pelx + 64:
                 hp -= 1 
                 vihu[1] = -160
                 vihu[0] = random.randint(50, 1000)


    #textin piirto
    texti = fontti.render("Elämiä jäljellä " + str(hp), True, tekstivari)
    ruutu.blit(pelaaja, (pelx,pely))
    ruutu.blit(texti, (30,30))
    pygame.display.flip()

# pelin loppu
def lanttu():
    ruutu.fill((255,0,0))
    pygame.display.flip()

# Pelin silmukka
while True:
    peruna()
    if hp > 0:
        porkkana()
    else:
        lanttu()
    ajastin.tick(FPS)