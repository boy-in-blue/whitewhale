import pygame
import sys
import random
import datetime

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
CHUNK = 64
SIZE = WIDTH, HEIGHT = 800, CHUNK*10
FISH_SIZE = FISH_WIDTH, FISH_HEIGHT = 32, 32

screen = pygame.display.set_mode(SIZE)
fish = pygame.image.load('fish32.png')
kelp = pygame.image.load('kelp.png')

fishPos = fish_x, fish_y = (WIDTH/3)-(FISH_WIDTH/2), (HEIGHT/2-FISH_HEIGHT/2)

fishMoveY = 0
obstacleMoveX = -5
obstacleSpawnX = WIDTH  # (2*WIDTH)/3


def fishDraw(x, y):
    return screen.blit(fish, (x, y))


def obstacleDraw(x):
    obs = pygame.Rect((x, 0, 1*CHUNK, random.randint(1, 6)*CHUNK))
    below_height = random.randint(
        1, HEIGHT/CHUNK - ((obs.height/CHUNK) + 3))*CHUNK
    obs_below = pygame.Rect((x, HEIGHT - below_height, CHUNK, below_height))
    return obs, obs_below


def detect_collision(fish_box, obs_box):
    return fish_box.colliderect(obs_box)


score = 0
line = []
for i in range(0, int(fish_x), 5):
    line.append([i, int(fish_y + FISH_HEIGHT/2)])
c = 0
obstacles = []
ticks = 0
while True:
    screen.fill((0, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                fishMoveY = -5
            if event.key == pygame.K_s:
                fishMoveY = 5
    fish_y += fishMoveY
    fb = fishDraw(fish_x, fish_y)

    line[-1] = (int(fish_x), int(fish_y + FISH_HEIGHT/2))
    for i in range(len(line)-1):
        line[i][1] = line[i+1][1]
    # c += 1
    # print(len(line))
    # print(line)
    for i in line:
        screen.set_at((i[0], i[1]), (0, 100, 255))
        screen.set_at((i[0]+1, i[1]+1), (0, 0, 255))
        screen.set_at((i[0], i[1]+1), (0, 0, 255))
        screen.set_at((i[0]+1, i[1]-1), (0, 100, 255))
        screen.set_at((i[0], i[1]-1), (0, 100, 255))
        screen.set_at((i[0]-1, i[1]-1), (0, 0, 255))
        screen.set_at((i[0]-1, i[1]), (0, 0, 255))
        screen.set_at((i[0]+1, i[1]+1), (0, 0, 255))
        screen.set_at((i[0]+1, i[1]), (0, 100, 255))

    # if c % int(fish_x) == 0:
        # c = 0
        

    if len(obstacles) == 0:
        obstacles.append(obstacleDraw(obstacleSpawnX))

    for obstacle in obstacles:
        obstacle[0].move_ip(obstacleMoveX, 0)
        a_left = obstacle[0].left
        a_top = obstacle[0].top
        a_width = obstacle[0].width
        a_height = obstacle[0].height
        if a_left <= 0:
            a_width = CHUNK + (a_left*CHUNK)
        for i in range(int(a_height/CHUNK)):

            screen.blit(kelp, pygame.draw.rect(
                screen, (0, 100, 100), (a_left, a_top, a_width, CHUNK)))
            a_top += CHUNK

        obstacle[1].move_ip(obstacleMoveX, 0)
        a_left = obstacle[1].left
        a_top = obstacle[1].top
        a_width = obstacle[1].width
        a_height = obstacle[1].height
        if a_left <= 0:
            a_width = CHUNK + (a_left*CHUNK)
        for i in range(int(a_height/CHUNK)):

            screen.blit(kelp, pygame.draw.rect(
                screen, (0, 100, 100), (a_left, a_top, a_width, CHUNK)))
            a_top += CHUNK

    if obstacles[-1][0].x < (2*WIDTH)/3:
        obstacles.append(obstacleDraw(obstacleSpawnX))

    if obstacles[0][0].x < 0-64:
        obstacles.pop(0)
        score += 1

    for obstacle in obstacles:
        if detect_collision(fb, obstacle[0]) or detect_collision(fb, obstacle[1]):
            print('dead', datetime.datetime.now().strftime("%S, %f"))
            score = 0

    if fish_y < 0 or fish_y > HEIGHT - FISH_HEIGHT:
        print('dead', datetime.datetime.now().strftime("%S, %f"))
        score = 0
        fishMoveY = 0

    pygame.display.update()
    if (ticks % 60 == 0):
        pass
        print(score)
        print(fpsClock.get_fps())
    ticks += 1
    fpsClock.tick(FPS)
# ideab y,me
