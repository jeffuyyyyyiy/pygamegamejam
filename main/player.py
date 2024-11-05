import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('main\sprites\player\pixil-frame-0.png') #placeholder
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1 #placeholder
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)