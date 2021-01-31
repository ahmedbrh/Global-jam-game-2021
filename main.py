import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
from subprocess import call
import os  
pygame.init()


vec = pygame.math.Vector2
HEIGHT = 500
WIDTH = 1000
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
backgroundim = pygame.image.load("bg2.png")    
joueur1image=pygame.image.load("joueur1.png")
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Les aventures de Ahmed: Ahmed retourne chez lui car il a oublié son masque")

run_ani_R = [ pygame.image.load("joueur1 (1).png"),pygame.image.load("joueur1 (2).png"),pygame.image.load("joueur1 (3).png"),pygame.image.load("joueur1 (4).png"),]
run_ani_L = [ pygame.image.load("joueur1gauche (1).png"),pygame.image.load("joueur1gauche (2).png"),pygame.image.load("joueur1gauche (3).png"),pygame.image.load("joueur1gauche (4).png"),]





class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.robot = True
            self.littleyounes=True
            self.bgimage = pygame.image.load("bg2.png")         
            self.bgY = 0
            self.bgX = 0
            self.map = 0
            self.marteaudispo = True
            self.marteaudirection="haut"
            self.martoY=300
            self.martoimage = pygame.image.load("marteau.png")
            self.premierpassage1 = True
            self.christopher=True
      def render(self,joueur):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))   
            if self.marteaudispo==True and self.map==0:
                
                    
                    
                    self.martoimage = pygame.image.load("marteau.png")
                    if self.martoY<=300:
                        self.marteaudirection="bas"
                    elif self.martoY>=340:
                        self.marteaudirection="haut"
                    if(self.marteaudirection=="haut"):
                        self.martoY-=0.10
                    else:
                        self.martoY+=0.10

                    if abs(640-joueur.pos.x)<=70 : 
                        self.martoimage = pygame.image.load("marteau - Copie.png")
                        
                    
                    displaysurface.blit(self.martoimage,(600,self.martoY))
                    
           

      def changemap(self,num):
        if(num==0):
            self.bgimage=pygame.image.load("bg2.png") 
        elif(num==1):
            
             self.bgimage=pygame.image.load("Sans titre(1) - Copie.png") 
        elif(num==2):
             self.bgimage=pygame.image.load("Sans titre(3) - Copie.png") 
        elif(num==3):
             self.bgimage=pygame.image.load("Sans titre(4).png")
        elif(num==4):
             self.bgimage=pygame.image.load("lastbackground.png")
            

      


               
 

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
        self.pos = vec((200, 430))
        self.vel = vec(0,0)
        self.direction = "RIGHT"
    

    def move(self, background):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.direction="LEFT"
            if pygame.time.get_ticks()>=self.timestamp+100:
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
        
        if self.pos.x>986 and self.pos.x<986.5:
            self.pos.x=20
            
            background.map+=1
            
            background.changemap(background.map)
            if(background.map-1==0 and background.premierpassage1):
                background.premierpassage1=False
            
        
                
               
            #Partie collisions avec les bords !
        elif self.pos.x>-0.5 and self.pos.x<0 and (background.map==0 and background.map!=2 and background.map!=3 ):
            self.pos.x=985
            background.map-=1

            background.changemap(background.map)
        elif self.pos.x>-0.5 and self.pos.x<0 and (background.map==0 or background.map==2 or background.map==3  ):
            self.pos.x=20
        
        self.rect.midbottom = self.pos
        ############################################################################################################


        
    def update(self):
      if self.move_frame ==4 :
            self.move_frame = 0
            return

       
 
    
class Panneau(pygame.sprite.Sprite):
    def __init__(self,nom):
        super().__init__()
        self.appear=True
        self.panneau = pygame.image.load(nom)
        self.boutonfermer = pygame.image.load("boutoncroix.png")
    
    def render(self):
        if self.appear==True:
            displaysurface.blit(self.panneau,(100,50))
            displaysurface.blit(self.boutonfermer,(780,50))
        

class Ennemi(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
lol = False
joueur = Joueur()
background = Background()
terrain = Terrain()
panneaulevel1=Panneau("panneaumarteau.png")
indiceunique=1
inventaireappear = False
panneau2 = Panneau("panneau2.png")
panneau3 = Panneau("panneau3.png")
panneau4 = Panneau("panneau4.png")
panneau5 = Panneau("panneau5.png")
panneau6 = Panneau("panneau6.png")
panneau7 = Panneau("panneau7.png")
panneau8 = Panneau("panneau8.png")
panneau9 = Panneau("panneau9.png")
panneau10 = Panneau("panneau10.png")
panneau11 = Panneau("panneau11.png")
panneau11.appear=False
panneau10.appear=False
panneau9.appear=False
panneau8.appear=False
panneau7.appear=True
booleanpanneau5=False
maskdirection="haut"
maskappear=True
repNon=False
maskX=185
maskY=330
maskimage = pygame.image.load("mask.png")
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
    if pygame.mouse.get_pressed()[0] : 
        print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    joueur.move(background)
    background.render(joueur)
    terrain.render()
    
    displaysurface.blit(joueur.image, joueur.rect)
    
    if abs(640-joueur.pos.x)<=70 and panneaulevel1.appear and background.map==0:
        
        panneaulevel1.render()
        if ((abs(pygame.mouse.get_pos()[0]-810)+abs(pygame.mouse.get_pos()[1]-60))<40 and pygame.mouse.get_pressed()[0]) or pygame.key.get_pressed()[K_e]:
            panneaulevel1.appear=False
            
       

            

    if   abs(640-joueur.pos.x)<=70 and pygame.key.get_pressed()[K_e]:
        background.marteaudispo=False
        inventaireappear = True
        

    
       
    if inventaireappear:
        displaysurface.blit(pygame.image.load("inventaire.png"), (870,20))
    if lol:
        displaysurface.blit(pygame.image.load("touches.png"), (joueur.pos.x,150))
        if abs(joueur.pos.x-750)<50 and pygame.key.get_pressed()[K_e] and background.map==1:
            inventaireappear=False
            lol = False
            background.littleyounes=False
            background.bgimage = pygame.image.load("Sans titre(2).png")  

    if background.map==1 and joueur.pos.x>=780 and joueur.pos.x<=800 and background.littleyounes==True:
            joueur.pos.x=780
   
            
            panneau2.render()
            if (  abs(pygame.mouse.get_pos()[0]-423)<83 and abs(pygame.mouse.get_pos()[1]-358)<18 and pygame.mouse.get_pressed()[0]     ):
                print("Jouez!")
                
                os.system('python Tictactoe.py')
            if ((abs(pygame.mouse.get_pos()[0]-810)+abs(pygame.mouse.get_pos()[1]-60))<40 and pygame.mouse.get_pressed()[0]):
                panneau2.appear=False
                
                if background.marteaudispo==False :
                    lol = True
               
    if background.map==2 and joueur.pos.x>=700 and joueur.pos.x<=720 and background.christopher==True:
            joueur.pos.x=700
            if repNon==False:
                if(booleanpanneau5==False and panneau3.appear):
                    panneau3.render()
                elif booleanpanneau5==False and panneau6.appear:
                    panneau6.render()
                    if ((abs(pygame.mouse.get_pos()[0]-810)+abs(pygame.mouse.get_pos()[1]-80))<60 and pygame.mouse.get_pressed()[0]):
                        panneau6.appear=False
                        background.christopher=False
                else:
                    panneau5.render()
                    if( ( (abs(pygame.mouse.get_pos()[1]-376)<=10 and abs(pygame.mouse.get_pos()[0]-220)<=10) or (abs(pygame.mouse.get_pos()[1]-376)<=10 and abs(pygame.mouse.get_pos()[0]-333)<=10) or
                    (abs(pygame.mouse.get_pos()[1]-374)<=10 and abs(pygame.mouse.get_pos()[0]-435)<=10) ) and  pygame.mouse.get_pressed()[0] and panneau5.appear ):
                        panneau4.appear=True
                        repNon=True
                    elif(abs(pygame.mouse.get_pos()[1]-376)<=10 and abs(pygame.mouse.get_pos()[0]-544)<=10 and pygame.mouse.get_pressed()[0] and panneau5.appear):
                        print("bonne réponse")
                        panneau6.appear==True
                        panneau5.appear=False
                        booleanpanneau5=False
                        
                
                if (((abs(pygame.mouse.get_pos()[1]-301)<36 and abs(pygame.mouse.get_pos()[0]-455)<74)or(abs(pygame.mouse.get_pos()[1]-297)<36 and abs(pygame.mouse.get_pos()[0]-653)<74))  and pygame.mouse.get_pressed()[0] and panneau3.appear and panneau5.appear==False  ):
                  
                    panneau3.appear=False
                    repNon=True
                elif(abs(pygame.mouse.get_pos()[1]-306)<36 and abs(pygame.mouse.get_pos()[0]-234)<74 and  pygame.mouse.get_pressed()[0] and panneau3.appear):
                    panneau5.render()
                    panneau5.appear=True
                    booleanpanneau5=True
                    panneau3.appear=False
                    
            else:
                panneau4.render()
                panneau4.appear=True
                
                if (abs(pygame.mouse.get_pos()[1]-309)<74 and abs(pygame.mouse.get_pos()[0]-459)<163  and pygame.mouse.get_pressed()[0]   ):
                    panneau4.appear=False
                    
                    repNon=False
                    panneau3.appear=True
                    panneau3.render()
            #Troisieme Map  Loop #################################################################
    if background.map==3 and joueur.pos.x>=600 and joueur.pos.x<=620 and background.robot==True:    
        joueur.pos.x=600
       
            
            
        if(abs(pygame.mouse.get_pos()[1]-340)<50 and abs(pygame.mouse.get_pos()[0]-250)<88 and  pygame.mouse.get_pressed()[0] ) and panneau7.appear:
            panneau8.appear=True
            panneau7.appear=False
               

        
        if(panneau9.appear):
            panneau9.render()
            if((abs(pygame.mouse.get_pos()[0]-810)+abs(pygame.mouse.get_pos()[1]-60))<40 and pygame.mouse.get_pressed()[0]):
                print("click!")
                background.robot=False
                panneau9.appear=False
        elif(panneau10.appear):
            panneau10.render()
            if((abs(pygame.mouse.get_pos()[0]-810)+abs(pygame.mouse.get_pos()[1]-60))<40 and pygame.mouse.get_pressed()[0]):
                print("click!")
                panneau7.appear=True
                panneau10.appear=False
        elif(panneau8.appear):
            panneau8.render()
        elif(panneau7.appear):
            panneau7.render()
            
        if ((abs(pygame.mouse.get_pos()[1]-206)<33 and abs(pygame.mouse.get_pos()[0]-501)<170)    or         (abs(pygame.mouse.get_pos()[1]-301)<33 and abs(pygame.mouse.get_pos()[0]-505)<170))and pygame.mouse.get_pressed()[0] and panneau8.appear:
            print("mauvaise reponse")
            panneau10.appear=True
            panneau8.appear=False
            
        elif (abs(pygame.mouse.get_pos()[1]-110)<33 and abs(pygame.mouse.get_pos()[0]-501)<170 and pygame.mouse.get_pressed()[0]) and panneau8.appear:
            print("bonne réponse")
            panneau9.appear=True
            panneau8.appear=False
            
        
        




        ##############################################################
    if background.map==4:
        if  panneau11.appear:
            panneau11.render()
        
        if maskappear:
            displaysurface.blit(maskimage,(maskX,maskY))
            if maskY<=300:
                maskdirection="bas"
            elif maskY>=350:
             maskdirection="haut"
            if(maskdirection=="haut"):
                maskY-=0.10
            else:
                maskY+=0.10
        if(joueur.pos.x>120 and joueur.pos.x<130):
            joueur.pos.x>120
            panneau11.appear=True
            maskappear=False

    
            
        
    
    pygame.display.update() 


    