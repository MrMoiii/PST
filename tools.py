import math
import time
class Map_liste:
    def __init__(self) -> None:
        self.liste = []
        self.liste.append(
            ('##########'
            '#   ##   #'
            '#        #'
            '#    ##  #'
            '##       #'
            '#   #    #'
            '#   #    #'
            '#   #    #'
            '#   #    #'
            '##########',10)
        )
class config:
    def __init__(self):

        self.SCREEN_HEIGHT = 320
        self.SCREEN_WIDTH = 480
        self.MAP_SIZE = 9
        self.TILE_SIZE = (self.SCREEN_WIDTH / self.MAP_SIZE)
        self.MAX_DEPTH = int(self.MAP_SIZE * self.TILE_SIZE)
        self.FOV = math.pi / 3
        self.HALF_FOV = self.FOV / 2
        self.CASTED_RAYS = 120
        self.STEP_ANGLE = self.FOV / self.CASTED_RAYS
        self.SCALE = (self.SCREEN_WIDTH ) / self.CASTED_RAYS
        fichier = open('map2.txt', 'r')
        self.MAP = ''.join(fichier.read().split('\n'))
        print(f'map :\n{self.MAP}')
        #self.MAP = Map_liste().liste[0]
class player:

    def __init__(self) -> None:
        SCREEN_HEIGHT = 480
        SCREEN_WIDTH = SCREEN_HEIGHT * 2
        self.x = (SCREEN_WIDTH / 2) / 2
        self.y = (SCREEN_WIDTH / 2) / 2
        self.angle_x = math.pi
        self.angle_y = math.pi
        self.speed = 3

    def add_angle(self,x,y):
        self.angle_x += x
        self.angle_y += y/10

    def move(self,x,y):
        self.x += x
        self.y += y

class balle:
    def __init__(self) -> None:
        self.liste = []
    
    def add(self,Config,Player):
        target_x = math.sin(Player.angle_x)
        target_y = math.cos(Player.angle_y)
        self.liste.append([Player.x+1,Player.y+1,[target_x,target_y]])
        print((target_x,target_y))



    def move(self):
        for i in self.liste:
            i[0] += i[2][0]
            i[1] += i[2][1]


class image:
    def __init__(self) -> None:
        self.liste = []
        self.fantome = False
    
    def add(self,image,chrono,pos):
        self.liste.append((image,time.time()+chrono,pos))

    def affiche(self,win,Config,Player):
        col = int(Player.x / Config.TILE_SIZE)
        row = int(Player.y / Config.TILE_SIZE)
        square = row * Config.MAP_SIZE + col
        if Config.MAP[square] == '?':
            fantome = True
        else:
            fantome = False
        
        if fantome and self.liste:
            win.blit(self.liste[0][0], self.liste[0][1])

        