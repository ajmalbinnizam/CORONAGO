import pygame
import random
# initialize pygame

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Space Shooter || സ്പേസ്")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('player.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
enemyimg = pygame.image.load('alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(0,100)
enemyX_change = 0.5
enemyY_change=40

def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


# gameloop, event in pygame, any click or move of mouse
running = True
while running:
    # pass
    screen.fill((0, 0, 0))  # RGB

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke pressed RIGHT OR LEFT
        if event.type == pygame.KEYDOWN:  # keypressed
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
        if event.type == pygame.KEYUP:  # keyreleased
            if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                playerx_change = 0

#checking boundary doesnt goes out of the bound
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736


    enemyX+= enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY+=enemyY_change
    elif enemyX >= 736:
        enemyX_change=-0.3
        enemyY+=enemyY_change

    enemy(enemyX, enemyY)
    player(playerx, playery)
    pygame.display.update()
