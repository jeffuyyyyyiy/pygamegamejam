import pygame
from main.scripts.player import Player
from main.scripts.gui import Gui
import shutil
import time
import json

#datasetup

database_file_path = 'main\Database\playerLocation.json'
map_file_path = 'main\Database\playerMap.json'

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

data = read_json(database_file_path)
mapdata = read_json(map_file_path)

#setup
width = 800
height = 440
pygame.init()
screen = pygame.display.set_mode((width, height)) #make it perhaps fixed to screen monitor size
clock = pygame.time.Clock()
player = Player(210, 210, 125, 125)
player.startThread()
running = True
startCutscenePlaying = data['startCutscenePlaying']
cutscene_starting_text = pygame.font.SysFont('Comic Sans MS', 16)

first_image = pygame.image.load('main\intro\intro1.png').convert_alpha()
second_image = pygame.image.load('main\intro\intro2.png').convert_alpha()
third_image = pygame.image.load('main\intro\intro3.png').convert_alpha()
fourth_image = pygame.image.load('main\intro\intro4.png').convert_alpha()

rain = pygame.mixer_music.load('main\Audio\intro_ambience.mp3')

map_house = pygame.image.load('main\sprites\mapSprites\map_house.png').convert_alpha()
map_outside = pygame.image.load('main\sprites\mapSprites\map_outside.png').convert_alpha()
map_outside1 = pygame.image.load('main\sprites\mapSprites\map_outside1.png').convert_alpha()


def playCutscene():
    cutscene_time = time.time()
    textalpha = 0
    firstalpha = 0
    fourthalpha = 255
    pygame.mixer_music.play()
    
    while time.time() - cutscene_time < 25:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    
        screen.fill("black")
        
        text = cutscene_starting_text.render("\"It was once said HE slept peacefully.\"", False, (255,255,255))
        #just reuse this variable ^^
        
        if time.time() - cutscene_time < 5:
            text.set_alpha(textalpha)
            if textalpha < 255:
                textalpha += 0.1
            screen.blit(text, (250, 370))
            pygame.display.flip()
        elif time.time() - cutscene_time < 15.6:
            first_imagerescaled = pygame.transform.scale(first_image, (800,440))
            first_imagerescaled_rect = first_imagerescaled.get_rect()
            first_imagerescaled.set_alpha(firstalpha)
            text.set_alpha(textalpha)
            if firstalpha < 170:
                firstalpha += 0.1
                
            if firstalpha > 150 and textalpha > 0:
                textalpha -= 0.1
            screen.blit(first_imagerescaled, first_imagerescaled_rect)
            screen.blit(text, (250, 370))
            pygame.display.flip()
        elif time.time() - cutscene_time < 15.8:
            second_imagerescaled = pygame.transform.scale(second_image, (800,440))
            second_imagerescaled_rect = second_imagerescaled.get_rect()
            screen.blit(second_imagerescaled, second_imagerescaled_rect)
            pygame.display.flip()
        elif time.time() - cutscene_time < 15.9:
            third_imagerescaled = pygame.transform.scale(third_image, (800,440))
            third_imagerescaled_rect = third_imagerescaled.get_rect()
            screen.blit(third_imagerescaled, third_imagerescaled_rect)
            pygame.display.flip()
        elif time.time() - cutscene_time < 20:
            fourth_imagerescaled = pygame.transform.scale(fourth_image, (800,440))
            fourth_imagerescaled_rect = fourth_imagerescaled.get_rect()
            fourth_imagerescaled.set_alpha(fourthalpha)
            if fourthalpha > 0:
                fourthalpha -= 0.1
            screen.blit(fourth_imagerescaled, fourth_imagerescaled_rect)
            pygame.display.flip()
        elif time.time() - cutscene_time < 23.5:
            text = cutscene_starting_text.render("\"An adventure awaits you.\"", False, (255,255,255))
            text.set_alpha(textalpha)
            if textalpha <= 255:
                textalpha += 0.1
            screen.blit(text, (300, 370))
            pygame.display.flip()
        elif time.time() - cutscene_time < 25:
            text = cutscene_starting_text.render("\"An adventure awaits you.\"", False, (255,255,255))
            text.set_alpha(textalpha)
            if textalpha > 0:
                textalpha -= 0.1
            screen.blit(text, (300, 370))
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

    player.movement(width, height)
    
    # fill the screen with a color to wipe away anything from last frame\
        
    match mapdata['location']:
        case "room":
            resized_map_house = pygame.transform.scale(map_house, (800, 440))
            resized_map_house_rect = resized_map_house.get_rect()
            screen.blit(resized_map_house, resized_map_house_rect)
        case "yard":
            resized_map_outside = pygame.transform.scale(map_outside, (800, 440))
            resized_map_outside_rect = resized_map_outside.get_rect()
            screen.blit(resized_map_outside, resized_map_outside_rect)
        case "street":
            resized_map_outside1 = pygame.transform.scale(map_outside1, (800, 440))
            resized_map_outside1_rect = resized_map_outside1.get_rect()
            screen.blit(resized_map_outside1, resized_map_outside1_rect)
    
    player.draw(screen)
    

    # RENDER YOUR GAME HERE
    if startCutscenePlaying:
        playCutscene()
        data['startCutscenePlaying'] = False
        startCutscenePlaying = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()

write_json(database_file_path, data)

#replace all images compressed using lossy compression into its normal resolution
def replacefolder(source, destination):
    temp = destination + "_temp"
    shutil.copytree(source,temp)
    shutil.rmtree(destination)
    shutil.move(temp, destination)
    
replacefolder('main\sprites\Backupplayer', 'main\sprites\player')
replacefolder('main\Backupintro', 'main\intro')
replacefolder('main\sprites\Backupmap', 'main\sprites\mapSprites')

exit()