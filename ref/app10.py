import pygame as pg
import sys

SIZE = WIDTH, HEIGHT = 800, 600
BLUE = (145, 196, 200)
YELLOW = (212, 210, 149)
BLACK = (0, 0, 0)
FPS = 60


class Sorting:
    def __init__(self):
        self.screen = None
        self.numbers = []
        self.font = None
        self.drawn = 0
        self.moving = False
        self.clock = None

    def create_scene(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.clock = pg.time.Clock()

    def background(self, color):
        self.screen.fill(color)

    def add_number(self, number: int):
        self.numbers.append([number, (0,0,0,0)])

    def add_numbers(self, numbers: list):
        for number in numbers:
            self.numbers.append([number, (0,0,0,0)])

    def draw_numbers_init(self):
        if not self.drawn:
            x_offset = 0
            for i in self.numbers:
                i[1] = pg.Rect(x_offset, 0, 100, 100)
                pg.draw.rect(self.screen, BLUE, i[1])
                self.screen.blit(self.font.render(str(i[0]), True, BLACK), (i[1].x + 32, i[1].y+32))
                x_offset += 120
        else:
            return
        self.drawn=1

    def draw_numbers(self):
        for i in self.numbers:
            pg.draw.rect(self.screen, BLUE, i[1])
            self.screen.blit(self.font.render(str(i[0]), True, BLACK), (i[1].x + 32, i[1].y+32))

    def move_numbers(self, src, dest):
        if not self.moving:
            if self.numbers[src][1].x != self.numbers[dest][1].x:
                self.numbers[src][1].x += 1
            else:
                self.numbers[dest]  = self.numbers[src]
                self.moving = True

    def swap_numbers(self, src, dest):
        localdest = self.numbers[dest][1].x
        localsrc = self.numbers[src][1].x
        if self.numbers[src][1].x != localdest:
            self.numbers[src][1].x += 1
        if self.numbers[src][1].x != localsrc:
            self.numbers[src][1].x -= 1

    def selection_sort(self):
        for i in range(len(self.numbers)):
            min_index = i
            for j in range(i+1, len(self.numbers)):
                if self.numbers[min_index] > self.numbers[j]:
                    min_index = j
            self.swap_numbers(i, min_index)
            print(1)
            self.numbers[i], self.numbers[min_index] = self.numbers[min_index], self.numbers[i]
            


if __name__ == '__main__':
    s = Sorting()
    s.create_scene()
    s.add_numbers([3,2,7, 45, 50])
    s.draw_numbers_init()
    move = s.selection_sort()
    while 1:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key in (pg.K_CAPSLOCK, pg.K_ESCAPE):
                    sys.exit()
                else:
                    pass
            else:
                pass

        s.background(YELLOW)
        s.draw_numbers_init()
        # print(s.numbers)
        move
        pg.time.delay(50)
        s.draw_numbers()
        pg.display.update()
        # print('tick')
        # s.clock.tick(FPS)
