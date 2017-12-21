import pygame
import time
import random

pygame.init()

display_width = 1240
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
transparent_red = (255,0,0,0.3)
green = (0, 255, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

boat_width = 75

backgorundImage = pygame.image.load('img/korea.jpg')
seaImage = pygame.image.load('img/bg1.png')
seaImage = pygame.transform.scale(seaImage, (1240, 720))
waveImage = pygame.image.load('img/wave.png')

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Escape North Korea')
clock = pygame.time.Clock()

rockImg = pygame.image.load('img/rock.png')
whaleImg = pygame.image.load('img/whale.png')
swimmerImage = pygame.image.load('img/ge1.png')
swimmerImage = pygame.transform.scale(swimmerImage, (75, 120))


def rocks(rockx, rocky, rockw, rockh):
    gameDisplay.blit(rockImg, [rockx, rocky, rockw, rockh])

def whale(whalex, whaley, whalew, whaleh):
    gameDisplay.blit(rockImg, [whalex, whaley, whalew, whaleh])

def wave(wavex, wavey, wavew, waveh):
    gameDisplay.blit(waveImage, [wavex, wavey, wavew, waveh])

def boat(x,y):
    gameDisplay.blit(swimmerImage,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    sailing_game()

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def button(mesage, x_coordinate, y_coordinate, width, height, color, action = None):
    click = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.rect(gameDisplay, color,(x_coordinate, y_coordinate, width, height))
    
    if x_coordinate + width > mouse_pos[0] > x_coordinate and y_coordinate + height > mouse_pos[1] > y_coordinate:
        if click[0] == 1 and action != None:
            action()

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(mesage, smallText)
    textRect.center = ( (x_coordinate + (width/2)), (y_coordinate + (height/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(backgorundImage, [0,0])
        largeText = pygame.font.SysFont("comicsansms",65)
        TextSurf, TextRect = text_objects("Escape North Korea", largeText)
        TextRect.center = ((display_width/2),(display_height/3.5))
        gameDisplay.blit(TextSurf, TextRect)

        button("Try Sailing to North Korea", ((display_width - 200)/2), 350, 200, 50, green, sailing_game)
        button("Try Running Trough DMZ", ((display_width - 200)/2), 450, 200, 50, red)
        button("Exit Game", ((display_width - 200)/2), 550, 200, 50, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def sailing_game():
    x = (display_width * 0.45)
    y = (display_height * 0.85)

    vertical_change = 0
    rock_starty = (random.randrange(100, 500) * (-1))
    rock_starty1 = (random.randrange(100, 300) * (-1))
    rock_speed = random.randrange(10, 15)
    rock_width = 100
    rock_height = 100

    rock_startx = random.randrange(0, display_width - (rock_width * 2))
    rock_startx1 = random.randrange(0, display_width - (rock_width * 2))

    wave_starty = -600
    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vertical_change = -10

                if event.key == pygame.K_RIGHT:
                    vertical_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    vertical_change = 0

        x += vertical_change
        gameDisplay.blit(seaImage, [0,0])

        wave(0, wave_starty, 1240, 1000)
        rocks(rock_startx, rock_starty, rock_width, rock_height)
        rocks(rock_startx1, rock_starty1, rock_width, rock_height)

        rock_starty += rock_speed
        rock_starty1 += rock_speed
        wave_starty += rock_speed
        boat(x,y)
        score(dodged)

        if x > display_width - boat_width or x < 0:
            crash()

        if wave_starty > (display_height / 2):
            wave_starty = 0 - 1000

        if rock_starty > display_height:
            rock_starty = 0 - rock_height - random.randrange(100, 700)
            rock_starty1 = 0 - rock_height
            rock_startx = random.randrange(0,display_width)
            rock_startx1 = random.randrange(0,display_width)
            dodged += 1

            if rock_speed < 20:
                rock_speed += 1.5

            rock_width += (dodged * 1.2)

        if y < rock_starty+rock_height:

            if x > rock_startx and x < rock_startx + rock_width or x+boat_width > rock_startx and x + boat_width < rock_startx+rock_width:
                message_display('You crashed to a rock')

        button("X", 1200, 20, 20, 20, transparent_red, game_intro)

        pygame.display.update()
        clock.tick(60)

game_intro()
sailing_game()
quitgame()
