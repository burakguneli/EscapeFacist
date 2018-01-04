import pygame
import time
import random

pygame.init()
pygame.mixer.init()

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
transparent_red = (255, 0, 0, 0.3)
green = (0, 170, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

boat_width = 75

text = pygame.font.Font('fonts/american.ttf', 40)

check = False

click = pygame.mouse.get_pressed()
mouse_pos = pygame.mouse.get_pos()

backgorundImage = pygame.image.load('img/korea.jpg')
southSuccessImage = pygame.image.load('img/gate.png')
southSuccessImage = pygame.transform.scale(southSuccessImage, (1280, 720))
looseImage = pygame.image.load('img/blizzardskull.png')
looseImage = pygame.transform.scale(looseImage, (1280, 720))

seaImage = pygame.image.load('img/bg1.png')
seaImage = pygame.transform.scale(seaImage, (1280, 720))

cityImage = pygame.image.load('img/city.jpg')
cityImage = pygame.transform.scale(cityImage, (1280, 720))

courtImage = pygame.image.load('img/courtroom.jpg')
courtImage = pygame.transform.scale(courtImage, (1280, 720))

coderImage = pygame.image.load('img/coder.jpg')
coderImage = pygame.transform.scale(coderImage, (1280, 720))

waveImage = pygame.image.load('img/wave.png')

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Escape North Korea')
clock = pygame.time.Clock()

rockImg = pygame.image.load('img/rock.png')
whaleImg = pygame.image.load('img/whale.png')

boatImage = pygame.image.load('img/ge1.png')
boatImage = pygame.transform.scale(boatImage, (75, 120))

trueImage = pygame.image.load('img/true_map.jpg')
trueImage = pygame.transform.scale(trueImage, (225, 360))

falseImage = pygame.image.load('img/wrong_map.jpg')
falseImage = pygame.transform.scale(falseImage, (225, 360))

soldierImage = pygame.image.load('img/soldier.png')
enemyImage = pygame.image.load('img/enemy.png')

bulletImage = pygame.image.load('img/bullet1.png')
bulletImage = pygame.transform.scale(bulletImage, (15, 25))

enemyBulletImage = pygame.image.load('img/upwardsBullet.png')
enemyBulletImage = pygame.transform.scale(enemyBulletImage, (15, 25))

wordArray = ["defmain", "whiletrue", "helloworld", "escapenorthkorea", "print", "complexity", "ifheadquarter", "construct", "structure", "displayblit"]
wordArraylen = len(wordArray)
