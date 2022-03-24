from tools import *
import pygame
import sys
import random as R
def cast_rays(win,Player,Config,Images):
    start_angle = Player.angle_x - Config.HALF_FOV
    col = int(Player.x / Config.TILE_SIZE)
    row = int(Player.y / Config.TILE_SIZE)
    for ray in range(Config.CASTED_RAYS):
        for depth in range(Config.MAX_DEPTH):
            target_x = Player.x - math.sin(start_angle) * depth
            target_y = Player.y + math.cos(start_angle) * depth
            col = int(target_x / Config.TILE_SIZE)
            row = int(target_y / Config.TILE_SIZE)
 
            square = row * Config.MAP_SIZE + col 
            if Config.MAP[square] == '#':
                color = 70 / (1 + depth * depth/2 * 0.00007)
                
                depth *= math.cos(Player.angle_x - start_angle)
                    
                wall_height = 19000 / (depth + 0.0001) 
                
                if wall_height > Config.SCREEN_HEIGHT: 
                    wall_height == Config.SCREEN_HEIGHT
                
                pygame.draw.rect(win,(color,color,color), (ray * Config.SCALE,((Config.SCREEN_HEIGHT / 2) - wall_height/2),Config.SCALE,wall_height))
                break
            """
            if Config.MAP[square] == '?':
                Images.affiche(win,Config,Player)
            """
    
        start_angle += Config.STEP_ANGLE

def Affiche_fps(win,clock):
    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont('Monospace Regular', 30)
    textsurface = font.render(fps, False, (255,255,255))
    win.blit(textsurface,(0,0))

def Gestion_move(keys,Player,Config):
    col = int(Player.x / Config.TILE_SIZE)
    row = int(Player.y / Config.TILE_SIZE)
    square = row * Config.MAP_SIZE + col
    

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        Player.move(math.cos(-Player.angle_x) * Player.speed,-math.sin(-Player.angle_x) * Player.speed)
        col = int(Player.x / Config.TILE_SIZE)
        row = int(Player.y / Config.TILE_SIZE)
        square = row * Config.MAP_SIZE + col
        if Config.MAP[square] == '#':
            Player.move(-math.cos(-Player.angle_x) * Player.speed,math.sin(-Player.angle_x) * Player.speed)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        Player.move(-math.cos(-Player.angle_x) * Player.speed,math.sin(-Player.angle_x) * Player.speed)
        col = int(Player.x / Config.TILE_SIZE)
        row = int(Player.y / Config.TILE_SIZE)
        square = row * Config.MAP_SIZE + col
        if Config.MAP[square] == '#':
            Player.move(math.cos(-Player.angle_x) * Player.speed,-math.sin(-Player.angle_x) * Player.speed)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        Player.move(-math.sin(Player.angle_x) * Player.speed,math.cos(Player.angle_x) * Player.speed)
        col = int(Player.x / Config.TILE_SIZE)
        row = int(Player.y / Config.TILE_SIZE)
        square = row * Config.MAP_SIZE + col
        if Config.MAP[square] == '#':
            Player.move(math.sin(Player.angle_x) * Player.speed,-math.cos(Player.angle_x) * Player.speed)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        Player.move(math.sin(Player.angle_x) * Player.speed,-math.cos(Player.angle_x) * 5)
        col = int(Player.x / Config.TILE_SIZE)
        row = int(Player.y / Config.TILE_SIZE)
        square = row * Config.MAP_SIZE + col
        if Config.MAP[square] == '#':
            Player.move(-math.sin(Player.angle_x) * 5,math.cos(Player.angle_x) * 5)

def Gestion_event(event,Player,Config):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
    if event.type == pygame.MOUSEMOTION:
        mouse_x,mouse_y = pygame.mouse.get_pos()
        mouse_x -= Config.SCREEN_WIDTH/2
        mouse_y -= Config.SCREEN_HEIGHT/2
        change_y = mouse_y
        change_x = mouse_x/500
        if change_x > 0.2:
            change_x = 0.2
        Player.add_angle(change_x,change_y)
        pygame.mouse.set_pos(Config.SCREEN_WIDTH/2,Config.SCREEN_HEIGHT/2)

def Alea_map(Config,Player):
    Config.MAP_SIZE = 9
    Config.MAP = ['' for i in range(9*9)]
    
    col = int(Player.x / Config.TILE_SIZE)
    row = int(Player.y / Config.TILE_SIZE)
    square = row * Config.MAP_SIZE + col
    for i in range(9):
        for j in range(9):
            Config.MAP.append("#" if R.randint(0,1) == 1 else " ")
    Config.MAP[square] = ' '
    Config.MAP = ''.join(Config.MAP)

def compdist(pos1,pos2):
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

def Afficher_Balles(win,Balles,Config,Player):
    for balle in Balles.liste:
        distance = compdist((Player.x,Player.y),(balle[0],balle[1]))
        target_x = math.sin(Player.angle_x)
        target_y = math.cos(Player.angle_y)
        but = int(distance/math.cos(Player.angle_x))
        pygame.draw.circle(win,(0,0,0), (but,int(Config.SCREEN_HEIGHT / 2)),int(50/distance*2))

def Afficher_sol(win,Config):
    j = 1
    
    for i in range(int(Config.SCREEN_HEIGHT/2),Config.SCREEN_HEIGHT,4):
        color = 50 / (1 + (i-int(Config.SCREEN_HEIGHT/2)) * (i-int(Config.SCREEN_HEIGHT/2)) * 0.00006)
        pygame.draw.rect(win,(color,color+50,color),(0,i,Config.SCREEN_WIDTH,i+4))
        j+=1