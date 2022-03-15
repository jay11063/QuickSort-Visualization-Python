import pygame
import sys
import random
from constants import *


class Bars:
    def __init__(self, high):
        self.arr = random.sample(range(1, high+1), high)
        self.high = high

    def reset_arr(self):
        # Shuffle
        for i in range(self.high-1, 1, -1):
            j = random.randint(0, i)
            self.swap(i, j)
            self.update(i, j)
        # self.arr = random.sample(self.arr, self.high)

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self, i, j):
        for idx, a in enumerate(self.arr):
            w = (WIDTH/self.high)
            h = int(a*(HEIGHT/self.high))
            # if idx==pivot:
            #     color = GREEN
            if idx == i or idx == j:
                color = COLOR_SET[color_number][2]
            else:
                color = COLOR_SET[color_number][1]
            pygame.draw.rect(screen, color, (int(idx*w), HEIGHT-h, int(w), h))

    def update(self, i=-1, j=-1):
        screen.fill(COLOR_SET[color_number][0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    change_color()
                elif event.key == pygame.K_ESCAPE:
                    self.quit()
        self.draw(i, j)
        pygame.display.update()
        fps.tick(60)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def quickSort(self, start, end):
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end
        while(left <= right):
            while(left <= end and self.arr[left] <= self.arr[pivot]):
                left += 1
            while(right > start and self.arr[right] >= self.arr[pivot]):
                right -= 1
            if(left > right):
                self.swap(right, pivot)
            else:
                self.swap(left, right)
            self.update(left, right)
        self.quickSort(start, right - 1)
        self.quickSort(right + 1, end)


def change_color():
    global color_number
    color_number += 1
    color_number %= len(COLOR_SET)


def main():
    bars = Bars(WIDTH//10)

    while True:
        bars.quickSort(0, bars.high - 1)
        # print(bars.arr)
        screen.fill(COLOR_SET[color_number][0])
        for idx, a in enumerate(bars.arr):
            w = int((WIDTH/bars.high))
            h = int(a*(HEIGHT/bars.high))
            pygame.draw.rect(
                screen, COLOR_SET[color_number][1], (idx*w, HEIGHT-h, w, h))
        pygame.display.update()
        # pygame.time.delay(600)
        bars.reset_arr()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Quick Sort')
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    main()
