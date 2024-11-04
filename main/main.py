import pygame
from player import Player

#setup
pygame.init()
screen = pygame.display.set_mode((420, 420), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

#sprites
#putspriteshere

#audio
#putaudiohere

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple") #porple borgler alam

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()