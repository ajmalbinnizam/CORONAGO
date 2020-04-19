import pygame
import random
import math
from pygame import mixer

# initialize pygame

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 533))

# background
background = pygame.image.load("coronaback.jpg")

# backgroundsound
mixer.music.load("background.wav")
mixer.music.play(-1)
# Title
pygame.display.set_caption("CORONA GO ")
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('dis.png')
playerx = 370
playery = 450
playerx_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numofenemies = 6

for i in range(numofenemies):
    enemyimg.append(pygame.image.load('coronavirus.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 35
bullet_state = "ready"

# font
score_val = 0
font = pygame.font.Font('digital-7.ttf', 34)
tetX = 10
textY = 10
cox = 290
coy = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
over = pygame.font.Font('freesansbold.ttf', 35)


def gameover():
    global back
    back = pygame.image.load("back.jpg")
    screen.blit(back, (0, 0))
    over_text =over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def corona(x, y):
    corona = over.render("GO CORONA", True, (255, 255, 255))
    screen.blit(corona, (x, y))

def show_score(x, y):
    score = font.render("SCORE :" + str(score_val), True, (255, 0, 0))
    screen.blit(score, (x, y))



def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance <34:
        return True
    else:
        return False


# gameloop, event in pygame, any click or move of mouse
running = True
while running:
    # pass
    screen.fill((0, 0, 0))  # RGB
    # back image
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke pressed RIGHT OR LEFT
        if event.type == pygame.KEYDOWN:  # keypressed
            if event.key == pygame.K_LEFT:
                playerx_change = -8
            if event.key == pygame.K_RIGHT:
                playerx_change = 8
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # get x co ordinate of space ship
                    bulletX = playerx
                    fire_bullet(playerx, bulletY)
        if event.type == pygame.KEYUP:  # keyreleased
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # checking boundary doesnt goes out of the bound
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    # enemy movement
    for i in range(numofenemies):
        # game over
        if enemyY[i]>480:
            for j in range(numofenemies):
                enemyY[j]=2000
            gameover()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]
            # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            col_sound = mixer.Sound("explosion.wav")
            col_sound.play()
            # bulletY = 480
            # bullet_state = "ready"
            score_val += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            enemyY[i] = random.randint(150, 300)
        enemy(enemyX[i], enemyY[i], i)
    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state =="fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerx, playery)
    show_score(tetX, textY)
    corona(cox, coy)
    pygame.display.update()
