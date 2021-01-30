import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
pygame.init()


vec = pygame.math.Vector2
HEIGHT = 500
WIDTH = 1000
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

joueur1image=pygame.image.load("joueur1.png")
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Les aventures de Ahmed")

run_ani_R = [ pygame.image.load("joueur1 (1).png"),pygame.image.load("joueur1 (2).png"),pygame.image.load("joueur1 (3).png"),pygame.image.load("joueur1 (4).png"),]
run_ani_L = [ pygame.image.load("joueur1gauche (1).png"),pygame.image.load("joueur1gauche (2).png"),pygame.image.load("joueur1gauche (3).png"),pygame.image.load("joueur1gauche (4).png"),]
 




class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("bg2.png")        
            self.bgY = 0
            self.bgX = 0
 
      def render(self):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))   
 
 
class Terrain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("t2.png")
        self.rect = self.image.get_rect(center = (500, 450))
 
    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))  
           
 
class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("joueur1.png")
        self.rect = self.image.get_rect()
        self.move_frame=0
        self.timestamp=pygame.time.get_ticks()
        self.vx = 0.35
        self.pos = vec((400, 430))
        self.vel = vec(0,0)
        self.direction = "RIGHT"

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.direction="LEFT"
            if pygame.time.get_ticks()>=self.timestamp+150:
                self.move_frame+=1
                self.update()
                self.image = run_ani_L[self.move_frame]
                self.timestamp=pygame.time.get_ticks()

            
            self.pos.x -= self.vx
            
        elif pressed_keys[K_RIGHT]:
            self.direction="RIGHT"
            if pygame.time.get_ticks()>=self.timestamp+150:
                self.move_frame+=1
                self.update()
                self.image = run_ani_R[self.move_frame]
                self.timestamp=pygame.time.get_ticks()
            self.pos.x += self.vx 

        
        else: 
            self.move_frame=0   
            if self.direction=="RIGHT":
                self.image = pygame.image.load("joueur1.png")
            else:
                self.image = pygame.image.load("joueur1gauche.png")
        self.rect.midbottom = self.pos
    def update(self):
      if self.move_frame ==4 :
            self.move_frame = 0
            return

       
 
    def attack(self):
        pass
    
    def jump(self):
        pass
 
class Ennemi(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()

joueur = Joueur()
background = Background()
terrain = Terrain()

while True:
       
    for event in pygame.event.get():
        # Pour fermer le jeu quand on clique sur le bouton fermer
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
             
        # Les actions à effectuer lors quand on fait un clic de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
 
        # Les actions à effectuer lors quand on fait un clic sur le clavier  
        if event.type == pygame.KEYDOWN:
              pass
    joueur.move()
    background.render()
    terrain.render()

    displaysurface.blit(joueur.image, joueur.rect)
    pygame.display.update() 


    