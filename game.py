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
swimmerImage = pygame.image.load('img/ge1.png')
swimmerImage = pygame.transform.scale(swimmerImage, (75, 120))


def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def rocks(rockx, rocky, rockw, rockh, color):
    #pygame.draw.rect(gameDisplay, color, [rockx, rocky, rockw, rockh])
    gameDisplay.blit(rockImg, [rockx, rocky, rockw, rockh])

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

    game_loop()

def crash():
    message_display('You crashed to a rock')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
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

        button("Start New Game",((display_width - 200)/2), 350, 200, 50, green, bright_green, game_loop)
        button("Continue Saved",((display_width - 200)/2), 450, 200, 50, red, bright_red)
        button("Exit Game",((display_width - 200)/2), 550, 200, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    thing_starty = -600
    thing_speed = random.randrange(11)
    thing_width = 100
    thing_height = 100

    thing_startx = random.randrange(0, display_width - thing_width)

    wave_starty = -600
    thingCount = 1
    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10

                if event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.blit(seaImage, [0,0])

        wave(0, wave_starty, 1240, 1000)
        rocks(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        wave_starty += thing_speed
        boat(x,y)
        score(dodged)

        if x > display_width - boat_width or x < 0:
            crash()

        if wave_starty > (display_height / 2):
            wave_starty = 0 - 1000

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1.5
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x+boat_width > thing_startx and x + boat_width < thing_startx+thing_width:
                crash()

        button("X",1200,20,20,20,transparent_red,transparent_red,game_intro)

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
quitgame()
