from globalVariables import *

decide1 = 0

def rocks(rockx, rocky, rockw, rockh):
    gameDisplay.blit(rockImg, [rockx, rocky, rockw, rockh])

def whale(whalex, whaley, whalew, whaleh):
    gameDisplay.blit(rockImg, [whalex, whaley, whalew, whaleh])

def wave(wavex, wavey, wavew, waveh):
    gameDisplay.blit(waveImage, [wavex, wavey, wavew, waveh])

def boat(x,y):
    gameDisplay.blit(boatImage, (x, y))

def soldier(x,y):
    gameDisplay.blit(soldierImage, (x, y))

def enemy(x,y):
    gameDisplay.blit(enemyImage, (x, y))

def bullet(x,y):
    gameDisplay.blit(bulletImage, (x, y))

def enemyBullet(x,y):
    gameDisplay.blit(enemyBulletImage, (x, y))

def wmap(x,y):
    gameDisplay.blit(falseImage, (x, y))

def tmap(x,y):
    gameDisplay.blit(trueImage, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fontInit = pygame.font.Font('fonts/american.ttf', 40)
    TextSurf, TextRect = text_objects(text, fontInit)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    if check == True:
        time.sleep(2)


def score(count, positionx, positiony):
    font = pygame.font.Font('fonts/american.ttf', 20)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text, (positionx, positiony))

def button(mesage, x_coordinate, y_coordinate, width, height, color, action = None):
    click = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.rect(gameDisplay, color, (x_coordinate, y_coordinate, width, height))

    smallText = pygame.font.Font("fonts/american.ttf", 14)
    textSurf, textRect = text_objects(mesage, smallText)
    textRect.center = ((x_coordinate + (width/2)), (y_coordinate + (height/2)))
    gameDisplay.blit(textSurf, textRect)
    pygame.draw.rect

    if x_coordinate + width > mouse_pos[0] > x_coordinate and y_coordinate + height > mouse_pos[1] > y_coordinate:
        if click[0] == 1 and action != None:
            action()
