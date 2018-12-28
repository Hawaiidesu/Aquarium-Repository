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
    
    print(v)
    return v
           
class player:
    x = 0
    y = 0
    sizeX = 50
    sizeY = 50
    speed = 1
    dashSpeed = 3
    
    
        
    collider_top = (0,0)
    collider_bottom = (0,0)
    collider_left = (0,0)
    collider_right = (0,0)
    
    collider_topleft = (0,0)
    collider_topright = (0,0)
    collider_bottomleft = (0,0)
    collider_bottomright = (0,0)
    
    def colliderUpdate():
        player.collider_top = (player.x + (player.sizeX / 2), player.y)
        player.collider_bottom = (player.x + (player.sizeX / 2), player.y + player.sizeY)
        player.collider_left = (player.x, player.y + (player.sizeY / 2))
        player.collider_right = (player.x + player.sizeX, player.y + (player.sizeY / 2))
        
        player.collider_topleft = (player.x, player.y)
        player.collider_topright = (player.x + player.sizeX, player.Y)
        player.collider_bottomleft = (player.x, player.y + player.sizeY)
        player.collider_bottomright = (player.x + player.sizeX, player.y + player.sizeY)
    
    def update():
        pygame.event.get()
        keys = pygame.key.get_pressed()
        step = 0
        
        player.colliderUpdate()
        
        if keys[pygame.K_LSHIFT]:
            step = player.dashSpeed
        else:
            step = player.speed
        
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if not (detectAll(scene.colliderList,player.collider_topleft[0],player.collider_topleft[1]) or detectAll(scene.colliderList,player.collider_topleft[0],player.collider_topleft[1])):
                player.y -= step
                
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not (detectAll(scene.colliderList,player.collider_bottomleft[0],player.collider_bottomleft[1]) or detectAll(scene.colliderList,player.collider_bottomleft[0],player.collider_bottomleft[1]))::
                player.y += step
                
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if not (detectAll(scene.colliderList,player.collider_topleft[0],player.collider_topleft[1]) or detectAll(scene.colliderList,player.collider_topleft[0],player.collider_topleft[1])):
                player.x -= step
                
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not detectAll(scene.colliderList,player.collider_right[0],player.collider_right[1]):
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

    