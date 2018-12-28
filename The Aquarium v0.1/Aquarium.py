import pygame
pygame.init()

# screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
screen = pygame.display.set_mode((1920,1080))
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


class collider:
    
    class get:
        
        def top(x,y,sizeX,sizeY):
            return (x + (sizeX / 2), y)
        
        def bottom(x,y,sizeX,sizeY):
            return (x + (sizeX / 2), y + sizeY)
        
        def left(x,y,sizeX,sizeY):
            return (x, y + (sizeY / 2))
        
        def right(x,y,sizeX,sizeY):
            return (x + sizeX, y + (sizeY / 2))
        
        def topleft(x,y,sizeX,sizeY):
            return (x, y)
        
        def topright(x,y,sizeX,sizeY):
            return (x + sizeX, y)
        
        def bottomleft(x,y,sizeX,sizeY):
            return (x, y + sizeY)
        
        def bottomright(x,y,sizeX,sizeY):
            return (x + sizeX, y + sizeY)         
        
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
    
    
def detect(x,y,x2,y2,x3,y3):
    return collider.detect(x,y,x2,y2,x3,y3)
    
def detectAll(listt,x,y):
    return collider.detectAll(listt,x,y)

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
        
        player.collider_top = collider.get.top(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_bottom = collider.get.bottom(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_left = collider.get.left(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_right = collider.get.left(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_topleft = collider.get.topleft(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_topright = collider.get.topright(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_bottomleft = collider.get.bottomleft(player.x,player.y,player.sizeX,player.sizeY)
        
        player.collider_bottomright = collider.get.bottomright(player.x,player.y,player.sizeX,player.sizeY)
    
    def update():
        pygame.event.get()
        keys = pygame.key.get_pressed()
        step = 0
        
        player.colliderUpdate()
        
        if keys[pygame.K_LSHIFT]:
            step = player.dashSpeed
        else:
            step = player.speed
        
        
        ctrlLeft = keys[pygame.K_LEFT] or keys[pygame.K_a]
        ctrlRight = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        ctrlUp = keys[pygame.K_UP] or keys[pygame.K_w]
        ctrlDown = keys[pygame.K_DOWN] or keys[pygame.K_s]
        
        detectDown = detectAll(scene.colliderList,player.collider_bottomleft[0],player.collider_bottomleft[1]) or detectAll(scene.colliderList,player.collider_bottomright[0],player.collider_bottomright[1])
        detectUp = detectAll(scene.colliderList,player.collider_topleft[0],player.collider_topleft[1]) or detectAll(scene.colliderList,player.collider_topright[0],player.collider_topright[1])
        detectRight = detectAll(scene.colliderList,player.collider_topright[0],player.collider_topright[1]) or detectAll(scene.colliderList,player.collider_bottomright[0],player.collider_bottomright[1])
        detectLeft = detectAll(scene.colliderList,player.collider_topleft[0],player.collider_topleft[1]) or detectAll(scene.colliderList,player.collider_bottomleft[0],player.collider_bottomleft[1])
        
        if ctrlUp:
            if not detectUp:
                player.y -= step
        
        if ctrlDown:
            if not detectDown:
                player.y += step
        
        if ctrlLeft:
            if not detectLeft:
                player.x -= step
        
        if ctrlRight:
            if not detectRight:
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

    