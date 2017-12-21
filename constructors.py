from globalVariables import *

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
