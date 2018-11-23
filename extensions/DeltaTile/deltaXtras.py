import pygame
import os
pygame.init()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def button(screen,action,posX,posY,sizeX,sizeY,hover,noHover):
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX > posX and mouseY > posY and mouseX < posX + sizeX and mouseY < posY + sizeY:
        if not (hover == 0 and noHover == 0):
            pygame.draw.rect(screen,hover,(posX,posY,sizeX,sizeY))
        if pygame.mouse.get_pressed()[0]:
            exec(action)
            pygame.time.delay(100)
    else:
        if not (hover == 0 and noHover == 0):
            pygame.draw.rect(screen,noHover,(posX,posY,sizeX,sizeY))
def font_load(fontt,size):
    return pygame.font.Font(fontt,size)

def dialouge(screenn,fontt,fontSize,text):
    # Box
    pygame.draw.rect(screenn,(0,0,0),(20,450,580,140)) #BG
    pygame.draw.rect(screenn,(255,255,255),(20,450,580,140),1) #BORDER
    textList = text.split('&*')
    i2 = 0
    while (i2 < len(textList)):
        screenn.blit(font_load(fontt,16).render(textList[i2], True, (255,255,255)), (22,452 + (i2*fontSize*1.2)))
        i2+=1
    

        
    