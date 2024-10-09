import pygame
from constants import *
from player import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
fps = pygame.time.Clock()
dt = 0

def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

    dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()