import pygame
import threading

class SpriteMap:
    def __init__(self, player, imgPath, posx, posy):
        #send initialized player class into SpriteMap contructor
        #client information should fully be transferred
        self.client = player
        self.image = pygame.image.load(imgPath)
        self.rect = self.image.get_rect()
        self.rect.topleft = (posx, posy)
        self.colliders = []
        
    #send collision constraints here must be rectangle
    #self.client.collision(direction)
    def collision(self):
        pass
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
        