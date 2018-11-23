import pygame
import deltaBase as deltaTile
import deltaXtras as ui
import os
from array import *

def clr():    
    os.system('cls' if os.name == 'nt' else 'clear')


activeKey = 'B'
activeMap = "BBAAAA; BAAAAA; AAAAAA: pfc_grass.png, A; pfc_stone.png, B; pfc_bricks.png, C"




fps = 60
x = 0
y = 0
size = 50
speed = 1
run = False

class col:
    white = (255,255,255)
    black = (0,0,0)
    gray = (100,100,100)

def clickToPlace():
    global x
    global y
    global activeMap
    global activeKey
    
    pygame.event.get()
    pos = pygame.mouse.get_pos()
    nX = round((pos[0]/size)+x)
    nY = round((pos[1]/size)+y)
    global activeMap
    activeMap = deltaTile.addMapCoord(activeMap,nX,nY,activeKey)
def programStart():
    print("Hey. You are using DeltaTile.")
    print("This project can be used in any way under the MIT License.")
    print("You can also use this for your games")
    print("DeltaTile is created by SkyanSam. The owner of Skylark Studios")
    
    global activeKey
    global activeMap
    print("")
    print("Do you want to open a existing map or make a new one?")
    inp = input("Open an existing map [O], Make new map [N]")
    if inp == "O":
        activeMap = input("Map data?")
    elif inp == "N":
        keyy = input("Key?")
        activeMap = (((("0"*10)+"; ")*9)+("0"*10)) + ": " + keyy
    
    activeKey = input("Active Key")
    
    
    print("Ok, Have fun making tilemaps")
    print("To quit press Q+Shift")
        

def endSave():
    global run
    
    run = False
    
    print("Thank you for using deltaTile")
    print("Do Ctrl+A and Ctrl+C to copy your map. Press Enter to copy your map.")
    input("")
    clr()
    print(activeMap)
    
    
    
def update():
    pygame.event.get()
    global x
    global y
    global activeKey
    x3 = x
    y3 = y
    
    print(activeKey)
    
    # BG
    screen.fill((0,0,0))
    
    # Tilemap
    deltaTile.drawTiles(screen,activeMap,x3,y,size,"tilepacks/pfc/")
    
    # Selector
    pos = pygame.mouse.get_pos()
    nX = round((pos[0]/size)+x3)*size
    nY = round((pos[1]/size)+y3)*size    
    pygame.draw.rect(screen,col.white,(nX,nY,size,size),1)
    
    # Events
    
    keys = pygame.key.get_pressed()
    
    # Movement
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_UP]:
        y -= speed
    
    # Active Keys
    if keys[pygame.K_a]:
        print('A')
        activeKey = 'A'
    if keys[pygame.K_b]:
        print('B')
        activeKey = 'B'
    if keys[pygame.K_c]:
        print('C')
        activeKey = 'C'
        
    
    
    
    # Mouse Click
    mse = pygame.mouse.get_pressed()
    if mse[0]:
        clickToPlace()
    
        
    
    
        
            
    

# deltaTile.drawTiles(deltaTile.mapp1,0,0,20,"tilepacks/pfc/")
# pygame.display.update()
# ui.dialouge(screen,"resources/font.ttf",18,"Hey there.&*IMMA EAT YOU ALIVE!!!!&*Looks like it worked! :)")
programStart()

pygame.init()
pygame.display.set_caption("DeltaTile Editor")
screen = pygame.display.set_mode((800,600))
pygame.display.update() 
run = True
while run:
    update()
    pygame.time.delay(round(1000 / fps))
    # update()
    # draw.main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    
    # Quit Key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] and keys[pygame.K_q]:
        pygame.quit()
        endSave()    

