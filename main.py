import sys
import pygame
from tools import *
from funcs import *
pygame.init()

Config = config()
Player = player()
Balles = balle()
Images = image()

#Initialisation de l'ecran
win = pygame.display.set_mode((Config.SCREEN_WIDTH,Config.SCREEN_HEIGHT), pygame.RESIZABLE)
#titre de la fenetre
pygame.display.set_caption("Let's GOOOOO")

clock = pygame.time.Clock()

#met la souris au centre de l'ecran et la rend invisible
pygame.mouse.set_pos(0,0)
pygame.mouse.set_visible(False)

Images.add(pygame.image.load("fantomatotr.png").convert_alpha(),5,((Config.SCREEN_WIDTH/2)-64,(Config.SCREEN_HEIGHT/2)-64))
#Boucle infinit principale
while True:
    #gestion de evenements pour fermer l'application 
    #et pour permettre de traquer la souris pour changer Player.angle_x
    for event in pygame.event.get():
        Gestion_event(event,Player,Config)

    
    #Affiche l'arrier plan (le sol et le ciel)
    Afficher_sol(win,Config)
    #pygame.draw.rect(win,(100,100,0),(0,Config.SCREEN_HEIGHT /2,Config.SCREEN_WIDTH,Config.SCREEN_HEIGHT))
    pygame.draw.rect(win,(200,100,0),(0,-Config.SCREEN_HEIGHT /2,Config.SCREEN_WIDTH,Config.SCREEN_HEIGHT))      
    
    #permet de visualiser la map du point de vue de Player.angle_x
    cast_rays(win,Player,Config,Images)
    Images.affiche(win,Config,Player)
    #Balles.move()  
    #Afficher_Balles(win,Balles,Config,Player)
    #Gestion de touches avec ESCAPE pour quitter
    #les touches de deplacement sont z,q,s,d
    keys = pygame.key.get_pressed()
    if keys:
        Gestion_move(keys,Player,Config) 
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)
    if keys[pygame.K_SPACE]:
        Balles.add(Config,Player)
        #Alea_map(Config,Player)
    if keys[pygame.K_LSHIFT]:
        Player.speed = 5
    else:
        Player.speed = 3

    if keys[pygame.K_LCTRL]:
        Player.speed = 1
    else:
        Player.speed = 3

    #permet de fixer le nombre d immages par seconde à 40 et affiche les fps en haut à gauche de l ecran
    clock.tick(30) 
    Affiche_fps(win,clock)

    pygame.display.flip()