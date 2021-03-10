import pygame
import random

pygame.init()

SIZE = W, H = 800, 600

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('my Game')
icon = pygame.image.load('./favicon.ico')
pygame.display.set_icon(icon)

pCoord = pX, pY = 400, 300
pXChange = 0
pYChange = 0

eXChange = 0
eYChange = 0

eX = -1
eY = 0

def player(coord):
    screen.blit(icon, coord)

def enemy(coord):
    screen.blit(icon, coord)

def enemy_move():
    leX = random.choice((-0.1, 0, 0.1))
    leY = random.choice((-0.1, 0, 0.1))
    return (leX, leY)

running = True

while running:

    screen.fill((100, 100, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pXChange = -0.1
            if event.key == pygame.K_RIGHT:
                pXChange = 0.1
            if event.key == pygame.K_UP:
                pYChange = -0.1
            if event.key == pygame.K_DOWN:
                pYChange = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pXChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pYChange = 0

    if pX < 0:
        pXChange = 0
        pX += 1
    if pX > W-128:
        pXChange = 0
        pX -= 1

    if pY < 0:
        pYChange = 0
        pY += 1
    if pY > H-128:
        pYChange = 0
        pY -= 1

    pX += pXChange
    pY += pYChange
    player((pX, pY))
    if eX < 0:
        eXChange = 0.1
    if eX > W-128:
        eXChange = -0.1
    eX += eXChange
    eY += eYChange
    enemy((eX, eY))
    pygame.display.update()
