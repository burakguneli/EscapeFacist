from constructors import *

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    pygame.mouse.set_visible(1)

    pygame.mixer.music.load("sound/sytlanta_title.mp3")
    pygame.mixer.music.play()

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
        button("Try Running Trough DMZ", ((display_width - 200)/2), 450, 200, 50, red, shooting_game)
        button("Exit Game", ((display_width - 200)/2), 550, 200, 50, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_won():

    pygame.mouse.set_visible(1)

    won = True

    while won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(southSuccessImage, [0,0])

        message_display('You are now in South Korea.')
        time.sleep(3)
        game_intro()

def game_lost():

    pygame.mouse.set_visible(1)

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

    pygame.mouse.set_visible(0)

    boat_x = (display_width * 0.45)
    boat_y = (display_height * 0.85)

    vertical_change = 0
    rock_starty = (random.randrange(100, 500) * (-1))
    rock_starty1 = (random.randrange(100, 300) * (-1))
    objects_speed = random.randrange(15, 20)
    land_counter = 36
    rock_width = 100
    rock_height = 100

    rock_startx = random.randrange(50, 800)
    rock_startx1 = random.randrange(50, 800)
    land_starty = -400

    wave_starty = -600

    pygame.mixer.music.load("sound/water.mp3")
    pygame.mixer.music.play()

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
        wave_starty += objects_speed + random.randrange(0, 5)
        land_starty += objects_speed

        if land_starty < -100:
            land_starty += objects_speed

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

                    pygame.draw.rect(gameDisplay, green,(0, land_starty, 1240, 200))

                    message_display("Congratulations!")
                    time.sleep(1)
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

def shooting_game():
    soldier_y = (display_height * 0.85)
    bullet_y = (display_height * 0.83)
    shoot_y = 0

    enemy_startx = random.randrange(50, 800)
    enemy_startx1 = random.randrange(50, 800)
    enemy_speed = random.randrange(5,10)

    enemy_starty = (random.randrange(100, 500) * (-1))
    enemy_starty1 = (random.randrange(100, 300) * (-1))

    firstCheck = 1
    firstCheck1 = 1

    shooter = True

    pygame.mouse.set_visible(0)

    while shooter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_intro()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_intro()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and shoot_y < 1:
                    shoot_y = bullet_y
                    shoot_x = x + 25
                    pygame.mixer.music.load("sound/bullet.mp3")
                    pygame.mixer.music.play()

        gameDisplay.blit(cityImage, [0,0])
        x,y = pygame.mouse.get_pos()
        soldier(x, soldier_y)

        enemy(enemy_startx, enemy_starty)
        enemy(enemy_startx1, enemy_starty1)

        enemy_starty += enemy_speed
        enemy_starty1 += enemy_speed

        if 10 < enemy_starty < display_height:
            if firstCheck == 1:
                bulletStart = enemy_starty
                firstCheck = 0

            bullet(enemy_startx, bulletStart)
            bulletStart += 25

            if bulletStart >= soldier_y and x < enemy_startx < (x + 50):
                message_display("You got shot!")
                time.sleep(1)
                game_lost()

        if 20 < enemy_starty1 < display_height:
            if firstCheck1 == 1:
                bulletStart1 = enemy_starty1
                firstCheck1 = 0

            bullet(enemy_startx1, bulletStart1)
            bulletStart1 += 25

            if bulletStart1 >= soldier_y and x < enemy_startx1 < (x + 50):
                message_display("You got shot!")
                time.sleep(1)
                game_lost()

        if enemy_starty > display_height:
            enemy_starty = -100 - random.randrange(100, 700)
            enemy_starty1 = -100
            enemy_startx = random.randrange(0, display_width)
            enemy_startx1 = random.randrange(0, display_width)

            firstCheck = 1
            firstCheck1 = 1

        if shoot_y > 0:
            bullet(shoot_x, shoot_y)
            shoot_y -= 45

        pygame.display.update()
        clock.tick(30)

game_intro()
sailing_game()
quitgame()
