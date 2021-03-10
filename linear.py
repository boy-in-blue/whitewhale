from app import Pygamer, BLUE, FPS, BLACK, BLUER, YELLOW
import pygame

RED = (255, 0, 0)

SIZE = WIDTH, HEIGHT = 800, 800

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


    def draw_vectors(self, scalar: list):
        pygame.draw.line(self.screen, RED, (WIDTH/2, HEIGHT/2), (WIDTH/2+scalar[0], HEIGHT/2+scalar[1]*-1))
                

if __name__ == '__main__':
    pgr = PygamerLA()
    pgr.start(SIZE)
    while pgr.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pgr.running = False
            elif event.type == pygame.KEYDOWN:
                pgr.kill_switch(event.key, [pygame.K_ESCAPE, pygame.K_CAPSLOCK])
            else:
                pass
                
        pgr.draw_background(BLUE)
        pgr.draw_grid(20)
        pgr.draw_vectors([20,20])
        pygame.display.update()
        pgr.clock.tick(FPS)
