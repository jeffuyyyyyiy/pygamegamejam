import pygame
from player import Player
from gui import Gui
from spriteMap import SpriteMap
import os
import shutil
import time
import threading
from pathlib import Path
from PIL import Image

#setup
width = 800
height = 440
pygame.init()
screen = pygame.display.set_mode((width, height)) #make it perhaps fixed to screen monitor size
clock = pygame.time.Clock()
player = Player(210, 210, 50, 50)
player.startThread()
running = True
startCutscenePlaying = True
cutscene_starting_text = pygame.font.SysFont('Comic Sans MS', 16)

first_image = pygame.image.load('main\intro\intro1.png').convert_alpha()
second_image = pygame.image.load('main\intro\intro2.png').convert_alpha()
third_image = pygame.image.load('main\intro\intro3.png').convert_alpha()
fourth_image = pygame.image.load('main\intro\intro4.png').convert_alpha()

def playCutscene():
    cutscene_time = time.time()
    
    while time.time() - cutscene_time < 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    
        screen.fill("black")
        
        text = cutscene_starting_text.render("test", False, (255,255,255))
        #just reuse this variable ^^
        
        if time.time() - cutscene_time < 2.5:
            first_imagerescaled = pygame.transform.scale(first_image, (800,440))
            first_imagerescaled_rect = first_imagerescaled.get_rect()
            screen.blit(first_imagerescaled, first_imagerescaled_rect)
            screen.blit(text, (400, 50))
            pygame.display.flip()
        elif time.time() - cutscene_time < 5:
            second_imagerescaled = pygame.transform.scale(second_image, (800,440))
            second_imagerescaled_rect = second_imagerescaled.get_rect()
            screen.blit(second_imagerescaled, second_imagerescaled_rect)
            pygame.display.flip()
        elif time.time() - cutscene_time < 7.5:
            third_imagerescaled = pygame.transform.scale(third_image, (800,440))
            third_imagerescaled_rect = third_imagerescaled.get_rect()
            screen.blit(third_imagerescaled, third_imagerescaled_rect)
            pygame.display.flip()
        elif time.time() - cutscene_time < 10:
            fourth_imagerescaled = pygame.transform.scale(fourth_image, (800,440))
            fourth_imagerescaled_rect = fourth_imagerescaled.get_rect()
            screen.blit(fourth_imagerescaled, fourth_imagerescaled_rect)
            pygame.display.flip()
        
#menuGui constructor

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window / alternative exit click esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
    screen.fill("black")

    player.movement(0, 0, width, height)
    
    # fill the screen with a color to wipe away anything from last frame
    
    player.draw(screen)

    # RENDER YOUR GAME HERE
    if startCutscenePlaying:
        playCutscene()
        startCutscenePlaying = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()

#replace all images compressed using lossy compression into its normal resolution
def replacefolder(source, destination):
    temp = destination + "_temp"
    shutil.copytree(source,temp)
    shutil.rmtree(destination)
    shutil.move(temp, destination)
    
replacefolder('main\sprites\Backupplayer', 'main\sprites\player')
replacefolder('main\Backupintro', 'main\intro')

exit()