import pygame
import math
import threading
import time

class Player:
    #instance variables
    
    #constructs player object
    def __init__(self, x, y):
        self.image = pygame.image.load('main\sprites\player\sl_down_idle.png')
        self.imageIndex = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1 #placeholder
        self.moving = False
        self.lastDeclaredDirection = "down"
    
    def incrementCounter(self):
        while True:
            self.imageIndex += 0.1
            time.sleep(0.025)
    
    def startThread(self):
        thread1 = threading.Thread(target=self.incrementCounter)
        thread1.start()
    
    #changes position of player depending on key input
    def movement(self, offsetx, offsety, width, height):
        keys = pygame.key.get_pressed()
        self.moving = False
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.rect.left > (0 + offsetx):
                self.lastDeclaredDirection = "left"
                self.moving = True
                self.rect.x -= self.speed
                self.animate(self.lastDeclaredDirection, self.moving)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.rect.right < (width - offsetx):
                self.moving = True
                self.rect.x += self.speed
                self.lastDeclaredDirection = "right"
                self.animate(self.lastDeclaredDirection, self.moving)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.top > (0 + offsety):
                self.moving = True
                self.rect.y -= self.speed
                self.lastDeclaredDirection = "up"
                self.animate(self.lastDeclaredDirection, self.moving)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.rect.bottom < (height - offsety):
                self.moving = True
                self.rect.y += self.speed
                self.lastDeclaredDirection = "down"
                self.animate(self.lastDeclaredDirection, self.moving)
        if self.moving == False:
            self.animate(self.lastDeclaredDirection, self.moving)
    
    #displays the player object in screen
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    #animation
    def animate(self, cardinal, moving):
        if moving:
            match cardinal:
                case "up":
                    if math.trunc(self.imageIndex) % 2 == 0:
                        self.image = pygame.image.load('main\sprites\player\sl_up.png')
                    elif math.trunc(self.imageIndex) % 2 == 1:
                        self.image = pygame.image.load('main\sprites\player\sl_up1.png')
                case "down":
                    if math.trunc(self.imageIndex) % 2 == 0:
                        self.image = pygame.image.load('main\sprites\player\sl_down.png')
                    elif math.trunc(self.imageIndex) % 2 == 1:
                        self.image = pygame.image.load('main\sprites\player\sl_down1.png')
                case "left":
                    if math.trunc(self.imageIndex) % 2 == 0:
                        self.image = pygame.image.load('main\sprites\player\sl_left.png')
                    elif math.trunc(self.imageIndex) % 2 == 1:
                        self.image = pygame.image.load('main\sprites\player\sl_left_idle.png')
                case "right":
                    if math.trunc(self.imageIndex) % 2 == 0:
                        self.image = pygame.image.load('main\sprites\player\sl_right.png')
                    elif math.trunc(self.imageIndex) % 2 == 1:
                        self.image = pygame.image.load('main\sprites\player\sl_right_idle.png')
        else:
            self.imageIndex = 0
            match cardinal:
                case "up":
                    self.image = pygame.image.load('main\sprites\player\sl_up_idle.png')
                case "down":
                    self.image = pygame.image.load('main\sprites\player\sl_down_idle.png')
                case "left":
                    self.image = pygame.image.load('main\sprites\player\sl_left_idle.png')
                case "right":
                    self.image = pygame.image.load('main\sprites\player\sl_right_idle.png')