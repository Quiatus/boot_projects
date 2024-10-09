import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = pygame.time.Clock()
dt = 0

def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen, (0,0,0))
    pygame.display.flip()

    dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()