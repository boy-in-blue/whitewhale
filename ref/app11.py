import pygame as pg
import sys
import numpy
import copy

SIZE = WIDTH, HEIGHT = 800, 600
BLUE = (145, 196, 200)
YELLOW = (212, 210, 149)
BLACK = (0, 0, 0)
BLUER = (83, 119, 133)


class Sorting:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.screen = None
        self.clock = None

    def init(self):
        pg.init()
        self.clock = pg.time.Clock
        self.screen = pg.display.set_mode(SIZE)

    def draw_background(self, color):
        self.screen.fill(color)

    def draw_graph(self, last_access=None):
        for index in range(len(self.numbers)):
            if last_access:
                if index in last_access:
                    color = BLUER
                else:
                    color = BLUE
            else:
                color = BLUE
            pg.draw.rect(self.screen, color,
                         (20*((2*index)+1),
                             0,
                             20,
                             self.numbers[index] * 20
                          ))

    def selection_sort(self):
        last_accessed = None
        for i in range(len(self.numbers)):
            min_index = i
            for j in range(i+1, len(self.numbers)):
                if self.numbers[min_index] > self.numbers[j]:
                    min_index = j
            self.numbers[i], self.numbers[min_index] = self.numbers[min_index], self.numbers[i]
            last_accessed = [i, min_index]
            yield last_accessed

    def bubble_sort(self):
        last_accessed = None
        for i in range(len(self.numbers)):
            for j in range(0, len(self.numbers) - i - 1):
                if self.numbers[j] > self.numbers[j+1]:
                    self.numbers[j], self.numbers[j +
                                                  1] = self.numbers[j+1], self.numbers[j]
                    last_accessed = [j, j+1]
                    yield last_accessed

    def insertion_sort(self):
        last_accessed = None
        for i in range(1, len(self.numbers)):
            key = self.numbers[i]
            j = i - 1
            while j >= 0 and key < self.numbers[j]:
                self.numbers[j+1] = self.numbers[j]
                last_accessed = [j, j+1]
                yield last_accessed
                j -= 1
            self.numbers[j + 1] = key
            last_accessed = [j+1, i]
            yield last_accessed

    # CHANGE THIS TO ITERATIVE INSTEAD OF RECURSIVE
    def merge_sort(self, n):
        last_accessed = None
        if len(n) > 1:
            mid = len(n)//2
            L = n[:mid]
            R = n[mid:]
            yield from self.merge_sort(L)
            yield from self.merge_sort(R)
            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    n[k] = L[i]
                    last_accessed = [k, k]
                    yield last_accessed
                    i += 1
                else:
                    n[k] = R[j]
                    last_accessed = [k, k]

                    yield last_accessed
                    j += 1
                k += 1

            while i < len(L):
                n[k] = L[i]
                last_accessed = [k, k]
                yield last_accessed
                i += 1
                k += 1
            while j < len(R):
                n[k] = R[j]
                last_accessed = [k, k]
                yield last_accessed
                j += 1
                k += 1


if __name__ == '__main__':
    lastaccessed = None
    is_sorted = False
    s = Sorting(numpy.random.randint(1, int(HEIGHT/20), 19).tolist())
    s.init()
    print(
        '''
        CAPSLOCK, ESC = exit
        S = selection sort
        B = bubble sort
        I = insertion sort
        M = merge sort (needs rework)
        '''
    )
    redraw_event = pg.USEREVENT + 1
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_CAPSLOCK, pg.K_ESCAPE):
                    sys.exit()
                elif event.key == pg.K_s:
                    if is_sorted:
                        s.numbers = numpy.random.randint(
                            1, int(HEIGHT/20), 19).tolist()
                        is_sorted = False
                    sort_yielder = s.selection_sort()
                    pg.time.set_timer(redraw_event, 50)
                elif event.key == pg.K_b:
                    if is_sorted:
                        s.numbers = numpy.random.randint(
                            1, int(HEIGHT/20), 19).tolist()
                        is_sorted = False
                    sort_yielder = s.bubble_sort()
                    pg.time.set_timer(redraw_event, 50)
                elif event.key == pg.K_i:
                    if is_sorted:
                        s.numbers = numpy.random.randint(
                            1, int(HEIGHT/20), 19).tolist()
                        is_sorted = False
                    sort_yielder = s.insertion_sort()
                    pg.time.set_timer(redraw_event, 50)
                elif event.key == pg.K_m:
                    if is_sorted:
                        s.numbers = numpy.random.randint(
                            1, int(HEIGHT/20), 19).tolist()
                        is_sorted = False
                    sort_yielder = s.merge_sort(s.numbers)
                    pg.time.set_timer(redraw_event, 50)
                else:
                    pass

            elif event.type == redraw_event:
                try:
                    nextyield = next(sort_yielder)
                    lastaccessed = nextyield
                except StopIteration:
                    lastaccessed = None
                    pg.time.set_timer(redraw_event, 0)
                    is_sorted = True
            else:
                pass
        s.draw_background(YELLOW)
        s.draw_graph(lastaccessed)
        pg.display.update()
