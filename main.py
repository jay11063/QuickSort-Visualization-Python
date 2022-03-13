import pygame
import sys
import random

# WIDTH, HEIGHT = 1920,1080
WIDTH, HEIGHT = 800, 400
BLACK = (0, 0, 0)
WHITE = (255,255,255)
# GREEN = (0,255,0)
GREEN = (100, 235, 66)
RED = (255,0,0)
# RED = (208, 49, 45)

class Bars:
    def __init__(self, high=100):
        self.arr = random.sample(range(1,high+1), high)
        self.high = high

    def reset_arr(self):
        self.arr = random.sample(range(1,self.high+1), self.high)

    def draw(self, screen, i, j):
        for idx, a in enumerate(self.arr):
            w = int((WIDTH/self.high))
            h = int(a*(HEIGHT/self.high))
            # if idx==pivot:
            #     color = GREEN
            if idx==i or idx==j:
                color = RED
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (idx*w, HEIGHT-h, w, h))
    
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
                self.swap(left,right)
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit()
            self.draw(screen, left, right)
            pygame.display.update()
            fps.tick(60)
        self.quickSort(start, right - 1)
        self.quickSort(right + 1, end)


def main():
    bars = Bars(400)

    while True:
        bars.quickSort(0, bars.high - 1)
        # print(bars.arr)
        screen.fill(BLACK)
        for idx, a in enumerate(bars.arr):
            w = int((WIDTH/bars.high))
            h = int(a*(HEIGHT/bars.high))
            pygame.draw.rect(screen, WHITE, (idx*w, HEIGHT-h, w, h))
        pygame.display.update()
        pygame.time.delay(600)
        bars.reset_arr()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Quick Sort')
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main()
