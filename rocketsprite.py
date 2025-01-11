import pygame

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
            self.rect.move_ip(0,-5)
        if keypressed[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if keypressed[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if keypressed[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

sprites=pygame.sprite.Group()

def startgame():
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
        
        pygame.display.update()


startgame()

