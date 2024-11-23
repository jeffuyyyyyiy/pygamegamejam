import pygame
import math
import threading
import time
from PIL import Image
from pathlib import Path
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
data = read_json('main\Database\playerMap.json')

class Player():
    #instance variables
    
    #constructs player object
    def __init__(self, x, y, sizex, sizey):
        self.scale(sizex, sizey)
        self.image = pygame.image.load('main\sprites\player\sl_down_idle.png')
        self.imageIndex = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1 #placeholder
        self.moving = False
        self.lastDeclaredDirection = "down"
        #collision
        self.collidedLeft = False
        self.collidedRight = False
        self.collidedUp = False
        self.collidedDown = False
    
    def incrementCounter(self):
        while True:
            self.imageIndex += 0.1
            time.sleep(0.025)
            
    def collisionHandler(self):
        while True:
            for currentLocation in data['locations']:
                if currentLocation['locationname'] == data['location']:
                    for collider in currentLocation['colliders']:
                        match collider['direction']:
                            case 'left':
                                if self.rect.left <= collider['terminateMovement']:
                                    if not self.rect.bottom <= collider['areaOfEffect'][0] or not self.rect.top >= collider['areaOfEffect'][1]:
                                        self.collision(collider['direction'])
                            case 'up':
                                if self.rect.top <= collider['terminateMovement']:
                                    if not self.rect.right <= collider['areaOfEffect'][0] or not self.rect.left >= collider['areaOfEffect'][1]:
                                        self.collision(collider['direction'])
                            case 'right':
                                if self.rect.right >= collider['terminateMovement']:
                                    if not self.rect.bottom <= collider['areaOfEffect'][0] or not self.rect.top >= collider['areaOfEffect'][1]:
                                        self.collision(collider['direction'])
                            case 'down':
                                if self.rect.bottom >= collider['terminateMovement']:
                                    if not self.rect.right <= collider['areaOfEffect'][0] or not self.rect.left >= collider['areaOfEffect'][1]:
                                        self.collision(collider['direction'])
    
    def startThread(self):
        thread1 = threading.Thread(target=self.incrementCounter)
        thread1.start()
        thread2 = threading.Thread(target=self.collisionHandler)
        thread2.start()
    
    #changes position of player depending on key input
    def movement(self, width, height):
        keys = pygame.key.get_pressed()
        self.moving = False
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.rect.left > 0 and not self.collidedLeft:
                self.lastDeclaredDirection = "left"
                self.moving = True
                self.rect.x -= self.speed
                self.animate(self.lastDeclaredDirection, self.moving)
                self.collidedRight = False
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.rect.right < width and not self.collidedRight:
                self.moving = True
                self.rect.x += self.speed
                self.lastDeclaredDirection = "right"
                self.animate(self.lastDeclaredDirection, self.moving)
                self.collidedLeft = False
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.top > 0 and not self.collidedUp:
                self.moving = True
                self.rect.y -= self.speed
                self.lastDeclaredDirection = "up"
                self.animate(self.lastDeclaredDirection, self.moving)
                self.collidedDown = False
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.rect.bottom < height and not self.collidedDown:
                self.moving = True
                self.rect.y += self.speed
                self.lastDeclaredDirection = "down"
                self.animate(self.lastDeclaredDirection, self.moving)
                self.collidedUp = False
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
                
    def collision(self, direction):
        match direction:
            case "left":
                self.collidedLeft = True
            case "right":
                self.collidedRight = True
            case "up":
                self.collidedUp = True
            case "down":
                self.collidedDown = True  
    
    def scale(self, sizex, sizey):
        folder_Path = 'main\sprites\player'
        path = Path(folder_Path)
        for file_path in path.rglob('*.*'):
            image = Image.open(file_path)
            new_size = (sizex, sizey)
            new_image = image.resize(new_size, Image.LANCZOS)
            new_image.save(file_path, format="PNG")
    