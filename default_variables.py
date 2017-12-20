import pygame
import time
import random

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
