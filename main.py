import pygame
import random

# initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# background image
bg = pygame.image.load('assets/bg1.png')



# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/feather.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('assets/spaceship.png')
playerX = 370
playerY = 500
playerX_change = 0
playerY_change = 0

# enemy
enemyImg = pygame.image.load('assets/ghost.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,100)
enemyX_change = 4
enemyY_change = 30

# bullets
bulletsImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 2      # bullet speed
bullet_state = 'ready' # can fire -> cant see bullet on screen



def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletsImg,(x+10,y+10))


# Game Infinite Loop
running = True
while running:
    # screen color RGB
    screen.fill((0,0,0))
    # background image
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change

    # boundary for x axis
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy boundary x axis
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # bullet movement
    if bulletY  <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()