import pygame

class Gui:
    def __init__(self, posx, posy, img):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.topleft = (posx, posy)
        
    def enabler(self, surface):
        keys = pygame.key.get_pressed()
        enabled = False
        if keys[pygame.K_TAB]:
            if enabled == False:
                enabled = True
            else:
                enabled = False
        
        if enabled == True:
            surface.blit(self.image, self.rect)

class HealthBar(Gui):
    pass