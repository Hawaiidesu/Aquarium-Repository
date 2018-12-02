import pygame
pygame.init()

screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)

fps = 60

pygame.display.set_caption("The Aquarium")

class mousePos:
    x = 0
    y = 0
    def get():
        pygame.event.get()
        pos = pygame.mouse.get_pos()
        mousePos.x = pos[0]
        mousePos.y = pos[1]

class scene:
    colliderList = [(500,500,700,700),(100,100,150,150)]
    def draw():
        pygame.draw.rect(screen,(0,255,0),(500,500,200,200))
        pygame.draw.rect(screen,(0,255,0),(100,100,50,50))

class pos:
    x = 0
    y = 0

def detect(x,y,x2,y2,x3,y3):
    if (x > x2 and x < x3) and (y > y2 and y < y3):
        v = True
    else:
        v = False
    return v

def detectAll(listt,x,y):
    i = 0
    v = False
    while i < len(listt):
        x2 = listt[i][0]
        y2 = listt[i][1] 
        x3 = listt[i][2]
        y3 = listt[i][3]
        
        if (x > x2 and x < x3) and (y > y2 and y < y3):
            v = True
        
        i += 1
        
    return v
           
class player:
    x = 0
    y = 0
    sizeX = 50
    sizeY = 50
    speed = 1
    dashSpeed = 3
    
    
        
    collider_top = (x + (sizeX / 2), y)
    collider_bottom = (x + (sizeX / 2), y + sizeY)
    collider_left = (x, y + (sizeY / 2))
    collider_right = (x + sizeX, y + (sizeY / 2))
        
    def update():
        pygame.event.get()
        keys = pygame.key.get_pressed()
        speed = 0
        
        if keys[pygame.K_LSHIFT]:
            step = player.dashSpeed
        else:
            step = player.speed
        
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not detectAll(scene.colliderList,player.collider_top[0],player.collider_top[1]):
                player.y -= step
                
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not detectAll(scene.colliderList,player.collider_bottom[0],player.collider_bottom[1]):
                player.y += step
                
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not detectAll(scene.colliderList,player.collider_left[0],player.collider_left[1]):
                player.x -= step
                
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not detectAll(scene.colliderList,player.collider_left[0],player.collider_left[1]):
                player.x += step
        
            
    def draw():
        pygame.draw.rect(screen,(255,0,0),(player.x,player.y,player.sizeX,player.sizeY))
    


def update():
    player.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    draw()
    pygame.display.update()    
    pygame.time.delay(round(1000 / fps))
    
def draw():
    screen.fill((0,0,0))
    player.draw()
    scene.draw()


while True:
    update()
    