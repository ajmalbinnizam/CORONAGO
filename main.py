import pygame

 # initialize pygame

pygame.init()

# create screen
screen=pygame.display.set_mode((800,600))

# Title
pygame.display.set_caption("Space Shooter || സ്പേസ്")
icon= pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# gameloop, event in pygame, any click or move of mouse
running=True
while running:
    # pass
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    pygame.display.update()