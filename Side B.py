import pygame
import random
pygame.init()
W,H = 1300, 600
SIZE = (W,H)
fps = pygame.time.Clock()
sc = pygame.display.set_mode((SIZE))

class Krugi():
    def __init__(self, x, y, radius, direkt, color=(156, 234, 0)):
        self.x, self.y =x, y
        self.color = color
        self.radius = radius
        self.direkt = direkt

    def draw(self, screen):    
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self):
        global change
        change = 1
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_a]:
           self.x -= 1
        if keys[pygame.K_d]:
            self.x += 1
        if keys[pygame.K_ESCAPE]:
            pygame.quit
            
        # if change == 1:
        #     if keys[pygame.K_SPACE]:
        #         self.color(30, 100, 255)  
        #         change = -1
        #         pygame.time.delay(100)

        # elif change == -1:
        #     if keys[pygame.K_SPACE]:
        #         self.color(30, 255, 100)  
        #         change = 1
        #         pygame.time.delay(100)
    
    def move_hor(self):
        if self.direkt == "right":
            self.x += 1
            if self.x > W:
                self.direkt = "left"
        else:
            self.x -=1
            if self.x < 0:
                self.direkt = "right"



running = True

circle_1 = Krugi(W//2, H//2, 25, (255, 100, 150))


list_of_circles=[]

for i in range (100):
    list_of_circles.append(Krugi(i * 10, i * 5, i + 10,'right', random.choices(range(0,256), k=3)))
    

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    sc.fill((0, 0, 0))
    
    circle_1.draw(sc)
    circle_1.move() 
    for j in list_of_circles:
        j.draw(sc)
        j.move_hor()       

    pygame.display.update()
        
    fps.tick(240)

