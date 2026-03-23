import pygame
import random

pygame.init()

ScreenW = 800
ScreenH = 600
scoreTenTime = 0

green = (0, 200, 0)
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)

clock = pygame.time.Clock()
enemyX1 = random.randint(0,800-25)

enemyY1 = 75

enemyX2 = random.randint(0,800-25)

enemyY2 = 75
enemySpeed = 3
enemyScore = 0
playerScore = 0

enemyScoreFont = pygame.font.SysFont(None, 30)
playerScoreFont = pygame.font.SysFont(None, 30)
playerWinFont = pygame.font.SysFont(None, 100)
playerLoseFont = pygame.font.SysFont(None, 100)

screen = pygame.display.set_mode((ScreenW, ScreenH))

player = pygame.Rect((400, 475, 50, 50)) 

enemy1 = pygame.Rect((enemyX1,enemyY1,25,25))
enemy2 = pygame.Rect((enemyX2,enemyY2,25,25))


gameStartFont = pygame.font.SysFont(None,85)

startButton = pygame.Rect((0,0, 200, 50))
startButton.center = (400,300)
startButtonFont = pygame.font.SysFont(None, 30)
startButtonColor = green

gameStart = False
run = True
while run:
    #
    mousePOS = pygame.mouse.get_pos()
    if startButton.collidepoint(mousePOS):
        startButtonColor = (green)
    else:
        startButtonColor = (red)

    #CLoses game when window is x out
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            #Resets game usinh key "R"
        if (playerScore >= 20 or enemyScore >= 5):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                playerScore = 0
                enemyScore = 0
                enemySpeed = 3
                enemyY1 = 75
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                run = False
        #
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.collidepoint(event.pos):
                gameStart = True

    #Displays Player Win Screen
    if playerScore >= 20:
        screen.fill((0,0,0))
            
        playerWinText = playerWinFont.render("You Win!!!", True, (white))
        playerWinRect = playerWinText.get_rect(center=(ScreenW // 2, ScreenH // 2))
        screen.blit(playerWinText, playerWinRect)

    #Displays Player Lose Screen
    elif enemyScore >= 5:
        screen.fill((0,0,0))
            
        playerLoseText = playerLoseFont.render("You LOSE", True, (white))
        playerLoseRect = playerLoseText.get_rect(center=(ScreenW // 2, ScreenH // 2))
        screen.blit(playerLoseText, playerLoseRect)

    elif gameStart == True:
        #Draws Screen
        screen.fill((black))

        #Draws Rectangle for player and Enemy
        pygame.draw.rect(screen, (red), player)
        pygame.draw.rect(screen, (red), enemy1)

        #Displays Player and Enemy Score Count
        enemyScoreText = enemyScoreFont.render(f"Enemy Score:  {enemyScore}", True, (white))
        screen.blit(enemyScoreText, (10,10))
        playerScoreText = playerScoreFont.render(f"Player Score:  {playerScore}", True, (white))
        screen.blit(playerScoreText, (630,10))
        #Physics for falling block
        enemyY1 += enemySpeed
        enemy1.y = enemyY1
        

        #Player Controls
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            player.move_ip(-10,0)
        elif key[pygame.K_d] == True:
            player.move_ip(10,0)

        #Player Colision for screen border
        if player.left < 0:
            player.left = 0
        if player.right > ScreenW:
            player.right = ScreenW
        if player.top < 0:
            player.top = 0
        if player.bottom > ScreenH:
            player.bottom = ScreenH

        #Increses Enemy Speed as player scores more points
        if playerScore > 5:
            enemySpeed = 5 
        if playerScore > 10:
            enemySpeed = 7
            if scoreTenTime == 0:
                scoreTenTime = pygame.time.get_ticks()
            currentTime = pygame.time.get_ticks()
            if currentTime - scoreTenTime > 3000:

                pygame.draw.rect(screen, (red), enemy2)
                enemyY2 += enemySpeed
                enemy2.y = enemyY2
        


        #Increments player score when blocking enemy block
        if player.colliderect(enemy1):
            enemyY1 = 75
            enemy1.y = enemyY1
            enemyX1 = random.randint(0,800-25)
            enemy1.x = enemyX1
            playerScore += 1
        if player.colliderect(enemy2):
            enemyY2 = 75
            enemy2.y = enemyY2
            enemyX2 = random.randint(0,800-25)
            enemy2.x = enemyX2
            playerScore += 1
        #Increments enemy score when enemy touches bottom of screen, then resets back to top
        if enemyY1 >= ScreenH:
            enemyY1 = 75
            enemy1.y = enemyY1
            enemyX1 = random.randint(0,800-25)
            enemy1.x = enemyX1
            enemyScore += 1
        if enemyY2 >= ScreenH:
            enemyY2 = 75
            enemy2.y = enemyY2
            enemyX2 = random.randint(0,800-25)
            enemy2.x = enemyX2
            enemyScore += 1
        # Game Start Logic
    else: 
        screen.fill((black))
        gameStartText = gameStartFont.render("Trash Collector", True, (white))
        gameStartTextBox = gameStartText.get_rect(center=(ScreenW // 2, 100))
        screen.blit(gameStartText,gameStartTextBox)
        pygame.draw.rect(screen, (startButtonColor), startButton)
        startButtonText = startButtonFont.render("Press Here to Start", True, (white))
        startButtonRect = startButtonText.get_rect(center=(400,300))
        screen.blit(startButtonText, startButtonRect)  

    pygame.display.update()
    clock.tick(60)
pygame.quit()