import pygame
from player import Player
from gui import Gui

#setup
width = 420
height = 420
pygame.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE) #make it perhaps fixed to screen monitor size
clock = pygame.time.Clock()
running = True
player = Player(210, 210)
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

    player.movement(0, 0, width, height)
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    player.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()