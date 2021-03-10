from app import Pygamer, BLUE, FPS, BLACK, BLUER, YELLOW
import pygame
import math

RED = (255, 0, 0)
GREEN = (255, 255, 0)
GAP = 20
FPS = 30

SIZE = WIDTH, HEIGHT = 800, 800

class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, vec2):
        x = self.x + vec2.x
        y = self.y + vec2.y
        return Vec2(x, y)

class PygamerLA(Pygamer):
    pass

    def draw_grid(self, gap):
        for i in range(0, WIDTH, gap):
            if i == WIDTH/2:
                pygame.draw.line(self.screen, BLACK, (i, 0), (i, HEIGHT))
            else:
                pygame.draw.line(self.screen, BLUER, (i, 0), (i, HEIGHT))

        for i in range(0, HEIGHT, gap):
            if i == HEIGHT/2:
                pygame.draw.line(self.screen, BLACK, (0, i), (WIDTH, i))
            else:
                pygame.draw.line(self.screen, BLUER, (0, i), (WIDTH, i))

    def draw_vectors(self, vec2: Vec2):
        vectorcoord = vx, vy = WIDTH/2+vec2.x*GAP, HEIGHT/2+vec2.y*-1*GAP
        pygame.draw.line(self.screen, RED, (WIDTH/2, HEIGHT/2), vectorcoord)

    def draw_vectors_from(self, vecfrom: Vec2, vecto: Vec2):
        vec_from = WIDTH/2+vecfrom.x*GAP, HEIGHT/2+vecfrom.y*-1*GAP
        vec_to = WIDTH/2+vecto.x*GAP, HEIGHT/2+vecto.y*-1*GAP
        pygame.draw.line(self.screen, GREEN, vec_from, vec_to)

if __name__ == '__main__':
    pgr = PygamerLA()
    pgr.start(SIZE)
    v1 = Vec2(5, 5)
    v2 = Vec2(3, 7)
    v3 = v1 + v2
    while pgr.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pgr.running = False
            elif event.type == pygame.KEYDOWN:
                pgr.kill_switch(event.key, [pygame.K_ESCAPE, pygame.K_CAPSLOCK])
            else:
                pass

        pgr.draw_background(BLUE)
        pgr.draw_grid(GAP)
        pgr.draw_vectors(v1)  # quad 1
        pgr.draw_vectors(v2)  # y+
        pgr.draw_vectors(v3)
        pgr.draw_vectors_from(v2, v3)
        # pgr.draw_vectors([10, -10], 20, math.pi/4)  # quad 2
        # pgr.draw_vectors([10, 0], 20, math.pi/4)  # x+
        # pgr.draw_vectors([-10, -10], 20, math.pi/4)  # quad 3
        # pgr.draw_vectors([-10, 0], 20, math.pi/4)  # x-
        # pgr.draw_vectors([-10, 10], 20, math.pi/4)  # quad 4
        # pgr.draw_vectors([0, -10], 20, math.pi/4)  # y-
        pygame.display.update()
        pgr.clock.tick(FPS)
