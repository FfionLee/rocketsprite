import pygame
import random

pygame.init()
screen=pygame.display.set_mode((600,600))

playing=True

bg=pygame.image.load('space.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('rocket.png')
        self.rect=self.image.get_rect()
    
    def update(self,keypressed):
        if keypressed[pygame.K_UP]:
            self.rect.move_ip(0,-2)
        if keypressed[pygame.K_DOWN]:
            self.rect.move_ip(0,2)
        if keypressed[pygame.K_LEFT]:
            self.rect.move_ip(-2,0)
        if keypressed[pygame.K_RIGHT]:
            self.rect.move_ip(2,0)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('meteor.png')
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x=random.randint(0,600)
        self.rect.y=random.randint(0,600)


sprites=pygame.sprite.Group()
obstaclegroup=pygame.sprite.Group()

def startgame():
    meteor=Obstacle()
    obstaclegroup.add(meteor)
    rocket=Player()
    sprites.add(rocket)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        keypressed=pygame.key.get_pressed()
        rocket.update(keypressed)
        screen.blit(bg,(0,0))
        sprites.draw(screen)
        obstaclegroup.draw(screen)
        meteor.update()
        
        pygame.display.update()


startgame()

