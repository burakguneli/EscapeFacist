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
southSuccessImage = pygame.image.load('img/gate.png')
southSuccessImage = pygame.transform.scale(southSuccessImage, (1240, 720))
lostImage = pygame.image.load('img/blizzardskull.png')
lostImage = pygame.transform.scale(lostImage, (1240, 720))

seaImage = pygame.image.load('img/bg1.png')
seaImage = pygame.transform.scale(seaImage, (1240, 720))

waveImage = pygame.image.load('img/wave.png')

gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Escape North Korea')
clock = pygame.time.Clock()

rockImg = pygame.image.load('img/rock.png')
whaleImg = pygame.image.load('img/whale.png')

boatImage = pygame.image.load('img/ge1.png')
boatImage = pygame.transform.scale(boatImage, (75, 120))


def rocks(rockx, rocky, rockw, rockh):
    gameDisplay.blit(rockImg, [rockx, rocky, rockw, rockh])

def whale(whalex, whaley, whalew, whaleh):
    gameDisplay.blit(rockImg, [whalex, whaley, whalew, whaleh])

def wave(wavex, wavey, wavew, waveh):
    gameDisplay.blit(waveImage, [wavex, wavey, wavew, waveh])

def boat(x,y):
    gameDisplay.blit(boatImage, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

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
    textRect.center = ((x_coordinate + (width/2)), (y_coordinate + (height/2)))
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
        largeText = pygame.font.SysFont("comicsansms", 35)
        TextSurf, TextRect = text_objects("Escape North Korea", largeText)
        TextRect.center = ((display_width/2), (display_height/3.5))
        gameDisplay.blit(TextSurf, TextRect)

        button("Try Sailing to North Korea", ((display_width - 200)/2), 350, 200, 50, green, sailing_game)
        button("Try Running Trough DMZ", ((display_width - 200)/2), 450, 200, 50, red, game_won)
        button("Exit Game", ((display_width - 200)/2), 550, 200, 50, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_won():

    won = True

    while won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(southSuccessImage, [0,0])

        message_display('You are now in South Korea. Congratulations!')
        time.sleep(3)
        game_intro()

def game_lost():

    lost = True

    while lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(lostImage, [0,0])

        message_display('You died. Redirecting to main menu')
        time.sleep(2)
        game_intro()

def sailing_game():
    boat_x = (display_width * 0.45)
    boat_y = (display_height * 0.85)

    vertical_change = 0
    rock_starty = (random.randrange(100, 500) * (-1))
    rock_starty1 = (random.randrange(100, 300) * (-1))
    objects_speed = random.randrange(15, 20)
    land_counter = 30
    rock_width = 100
    rock_height = 100

    rock_startx = random.randrange(50, 800)
    rock_startx1 = random.randrange(50, 800)

    wave_starty = -600

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

        boat_x += vertical_change
        gameDisplay.blit(seaImage, [0,0])

        wave(0, wave_starty, 1240, 1000)
        rocks(rock_startx, rock_starty, rock_width, rock_height)
        rocks(rock_startx1, rock_starty1, rock_width, rock_height)

        rock_starty += objects_speed
        rock_starty1 += objects_speed
        wave_starty += objects_speed
        boat(boat_x, boat_y)

        if wave_starty > (display_height / 2):
            wave_starty = -1000

        if boat_x > display_width - boat_width or boat_x < 0:
            crash()

        if rock_starty > display_height:
            rock_starty = 0 - rock_height - random.randrange(100, 700)
            rock_starty1 = 0 - rock_height
            rock_startx = random.randrange(0, display_width)
            rock_startx1 = random.randrange(0, display_width)

            if objects_speed < 30: #max speed
                objects_speed += 1.5

            if objects_speed >= 30:
                land_counter += 2

                if land_counter == 40:
                    game_won()

        if boat_y < rock_starty + rock_height:

            if boat_x > rock_startx and boat_x < rock_startx + rock_width or boat_x + boat_width > rock_startx and boat_x + boat_width < rock_startx + rock_width:
                message_display('You crashed to a rock')
                time.sleep(1)
                game_lost()

        if boat_y < rock_starty1 + rock_height:

            if boat_x > rock_startx1 and boat_x < rock_startx1 + rock_width or boat_x + boat_width > rock_startx1 and boat_x + boat_width < rock_startx1 + rock_width:
                message_display('You crashed to a rock')
                time.sleep(1)
                game_lost()

        button("X", 1200, 20, 20, 20, transparent_red, game_intro)

        pygame.display.update()
        clock.tick(30)

game_intro()
sailing_game()
quitgame()
