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
        largeText = pygame.font.Font("fonts/american.ttf", 25)
        TextSurf, TextRect = text_objects("Escape North Korea", largeText)
        TextRect.center = ((display_width/2), 50)
        gameDisplay.blit(TextSurf, TextRect)

        button("Try Sailing to North Korea", ((display_width - 200)/2), 100, 220, 50, green, sailing_game)
        button("Try Running Trough DMZ", ((display_width - 200)/2), 200, 220, 50, green, shooting_game)
        button("Code to Open Gates", ((display_width - 200)/2), 300, 220, 50, green, code_to_Escape)
        button("Go to Europe", ((display_width - 200)/2), 400, 220, 50, green, escape_to_Europe)
        button("Asia Underground Railroad", ((display_width - 200)/2), 500, 220, 50, green, find_map)
        button("Exit Game", ((display_width - 200)/2), 600, 220, 50, red, quitgame)

        pygame.display.update()
        clock.tick(30)


def game_won():

    pygame.mouse.set_visible(1)

    won = True

    while won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(southSuccessImage, [0,0])

        message_display('You managed to escape from North Korea!')
        time.sleep(3)
        game_intro()

def game_lost():

    pygame.mouse.set_visible(1)

    lost = True

    while lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(looseImage, [0,0])

        message_display('You died. Redirecting to main menu')
        time.sleep(2)
        game_intro()


def sailing_game():

    pygame.mouse.set_visible(1)

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

        wave(0, wave_starty, 1280, 1000)

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

                    pygame.draw.rect(gameDisplay, green,(0, land_starty, 1280, 200))

                    message_display("Congratulations!")
                    time.sleep(1)
                    game_won()

        if boat_y < rock_starty + rock_height and rock_starty < display_height:

            if boat_x > rock_startx and boat_x < rock_startx + rock_width or boat_x + boat_width > rock_startx and boat_x + boat_width < rock_startx + rock_width:
                message_display('You crashed to a rock')
                time.sleep(1)
                game_lost()

        if boat_y < rock_starty1 + rock_height and rock_starty1 < display_height:

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
    shoot_y = -1000

    enemy_startx = random.randrange(50, 800)
    enemy_startx1 = random.randrange(50, 800)
    enemy_speed = random.randrange(5,10)

    enemy_starty = (random.randrange(100, 500) * (-1))
    enemy_starty1 = (random.randrange(100, 300) * (-1))

    firstCheck = 1
    firstCheck1 = 1

    dodged = 0

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
        x, y = pygame.mouse.get_pos()
        soldier(x, soldier_y)

        enemy(enemy_startx, enemy_starty)
        enemy(enemy_startx1, enemy_starty1)

        enemy_starty += enemy_speed
        enemy_starty1 += enemy_speed


        if 10 < enemy_starty < display_height:
            if firstCheck == 1:
                bulletStart = enemy_starty
                firstCheck = 0

            enemyBullet(enemy_startx, bulletStart)
            bulletStart += 25

            if soldier_y <= bulletStart <= display_height and x < enemy_startx < (x + 50):
                message_display("You got shot!")
                time.sleep(1)
                game_lost()

        if 20 < enemy_starty1 < display_height:
            if firstCheck1 == 1:
                bulletStart1 = enemy_starty1
                firstCheck1 = 0

            enemyBullet(enemy_startx1, bulletStart1)
            bulletStart1 += 25

            if soldier_y <= bulletStart1 <= display_height and x < enemy_startx1 < (x + 50):
                message_display("You got shot!")
                time.sleep(1)
                game_lost()

        #shooting enemy soldiers
        if ((enemy_starty + 80) > shoot_y > enemy_starty) and (x < enemy_startx < (x + 220)):
            enemy_starty = 900
            dodged += 1
            shoot_y = -1000

        if  ((enemy_starty1 + 80) > shoot_y > enemy_starty1) and (x < enemy_startx1 < (x + 220)):
            enemy_starty1 = 900
            dodged += 1
            shoot_y = -1000

        #getting shot by enemy
        if enemy_starty > display_height:
            enemy_starty = -100 - random.randrange(100, 700)
            enemy_startx = random.randrange(0, display_width)
            firstCheck = 1
            dodged += 1

        if enemy_starty1 > display_height:
            enemy_starty1 = -100
            enemy_startx1 = random.randrange(0, display_width)
            firstCheck1 = 1
            dodged += 1

        if shoot_y > 0:
            bullet(shoot_x, shoot_y)
            shoot_y -= 45

        if dodged > 40:
            game_won()

        score(dodged, 10, 0)
        pygame.display.update()
        clock.tick(30)


def switch_answers(argument):
    switcher = {
        "yes": 'Where are you from?',
        "yeah": 'You are rood. Where are you from?',
        "pyongyang": 'How did you came here?',
        "shenyang": 'You said you were coming from North Korea. Shenyang is in China! You are under arrest!',
        "plane": 'How did you buy a seat on a plane which comes to Europe?',
        "car": "How did you passed China?",
        "usedfakeid": "Congratulations sir you can continue your life in Europe",
        "oops": "You Lied! We aresenting you back!",
    }
    return (switcher.get(argument, "Invalid answer"))

def avaibleWords(argument):
    switcher = {
        0: 'yes, yeah',
        1: 'pyongyang, shenyang',
        2: 'plane, car',
        3: 'usedfakeid, oops',
    }
    return (switcher.get(argument, "Invalid"))

def escape_to_Europe():

    pygame.mixer.music.load("sound/courtroom.mp3")
    pygame.mixer.music.play()

    text = pygame.font.Font('fonts/american.ttf', 25)

    questionCounter = 0

    typedWord = ""
    textsurface = text.render('So you are coming from North Korea. Right?', True, (0, 0, 0))

    escapeEurope = True

    while escapeEurope:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_intro()

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                if event.key == pygame.K_ESCAPE:
                    game_intro()

                if event.key == pygame.K_BACKSPACE:
                    typedWord = typedWord[:-1]

                if len(key) == 1:
                    typedWord += pygame.key.name(event.key)

        gameDisplay.blit(courtImage, [0,0])

        if typedWord == "yes" or typedWord == "yeah" or typedWord == "pyongyang" or typedWord == "shenyang" or typedWord == "plane" or typedWord == "car" or typedWord == "usedfakeid" or typedWord == "oops":
            questionCounter += 1
            textsurface = text.render(switch_answers(typedWord), True, (0, 0, 0))

        textsurface1 = text.render("Your answer: " + typedWord, True, white)
        textsurface2 = text.render("Avaiable word list: " + avaibleWords(questionCounter), True, white)

        gameDisplay.blit(textsurface ,(100, 50))
        gameDisplay.blit(textsurface1, (100, 650))
        gameDisplay.blit(textsurface2, (100, 600))

        pygame.display.update()

        if typedWord == "shenyang" or typedWord == "oops":
            time.sleep(2)
            game_lost()

        if typedWord == "usedfakeid":
            time.sleep(2)
            game_won()

        if typedWord == "yes" or typedWord == "yeah" or typedWord == "pyongyang" or typedWord == "shenyang" or typedWord == "plane" or typedWord == "car" or typedWord == "usedfakeid" or typedWord == "oops":
            typedWord = ""

        clock.tick(30)


def code_to_Escape():

    wordx = 0
    wordy = random.randrange(100, 400)
    selector = random.randrange(0, wordArraylen)
    typedWord = ""
    success = 0
    baseUp = 10
    initial_time = 0

    pygame.mixer.music.load("sound/hackeffect.mp3")
    pygame.mixer.music.play()

    text = pygame.font.Font('fonts/american.ttf', 20)

    code = True

    while code:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_intro()

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                if event.key == pygame.K_ESCAPE:
                    game_intro()

                if event.key == pygame.K_BACKSPACE:
                    typedWord = typedWord[:-1]

                if len(key) == 1:
                    typedWord += pygame.key.name(event.key)

        gameDisplay.fill(black)

        if initial_time > 20:
            textsurface = text.render("Your goal is to hack North Korea's borders password", True, white)
            gameDisplay.blit(textsurface, (50, 50))

        if initial_time > 80:
            textsurface1 = text.render("You need to type faster than syber securities!", True, white)
            gameDisplay.blit(textsurface1, (50, 100))

        if initial_time > 140:
            textsurface2 = text.render("If you can reach 500 points you will win", True, white)
            gameDisplay.blit(textsurface2, (50, 150))

        if initial_time > 190:
            textsurface3 = text.render("Get ready game is about to begin!", True, white)
            gameDisplay.blit(textsurface3, (50, 200))

        if initial_time > 230:
            gameDisplay.blit(coderImage, [0, 0])

            if wordx < (display_width + 5):
                wordx += baseUp
            if wordx > display_width:
                wordx = 0
                typedWord = ""
                selector = random.randrange(0, wordArraylen)
                wordy = random.randrange(100, 400)

            if typedWord == wordArray[selector]:
                success += 1

            if len(typedWord) >= len(wordArray[selector]) and typedWord != wordArray[selector]:
                success -= 0.5

            if success > 300:
                game_won()

            if success < -50:
                game_lost()

            textsurface = text.render(wordArray[selector], True, green)
            gameDisplay.blit(textsurface, (wordx, wordy))

            textsurface1 = text.render("Your word: " + typedWord, True, white)
            gameDisplay.blit(textsurface1, (750, 600))

            score(success, (display_width - 150), 0)

        initial_time += 1

        pygame.display.update()
        clock.tick(30)


def find_map():

    text = pygame.font.Font('fonts/american.ttf', 20)

    typedWord = ''
    initial_time = 0

    findMap = True

    while findMap:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_intro()

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                if event.key == pygame.K_ESCAPE:
                    game_intro()

                if event.key == pygame.K_BACKSPACE:
                    typedWord = typedWord[:-1]

                if len(key) == 1:
                    typedWord += pygame.key.name(event.key)

        gameDisplay.fill(black)

        if initial_time > 20:
            textsurface = text.render("Asia Underground Railroad is a very though road", True, white)
            gameDisplay.blit(textsurface, (50, 50))

        if initial_time > 80:
            textsurface1 = text.render("But if you can manage to find the right path, you can escape!", True, white)
            gameDisplay.blit(textsurface1, (50, 100))

        if initial_time > 140:
            textsurface2 = text.render("But unfortunetly, North Korean and Chineese Government changed the map", True, white)
            gameDisplay.blit(textsurface2, (50, 150))

        if initial_time > 190:
            textsurface3 = text.render("You need to choose the right map!", True, white)
            gameDisplay.blit(textsurface3, (50, 200))

        if initial_time > 230:
            textsurface5 = text.render("Right map contains a red base close to 'TORP'", True, white)
            gameDisplay.blit(textsurface5, (50, 250))

        if initial_time > 280:
            wmap(385, 300)

        if initial_time > 310:
            tmap(620, 300)

        if initial_time > 330:
            textsurface6 = text.render("Which one is true map? first or second?: " + typedWord, True, white)
            gameDisplay.blit(textsurface6, (380, 700))

        if typedWord == 'first' or typedWord == '1':
            gameDisplay.fill(black)
            message_display('You selected the wrong one!')
            time.sleep(3)
            game_lost()

        if typedWord == 'second' or typedWord == '2':
            gameDisplay.fill(black)
            message_display('You selected the right one!')
            time.sleep(3)
            game_won()

        initial_time += 1

        pygame.display.update()
        clock.tick(30)

game_intro()
quitgame()
