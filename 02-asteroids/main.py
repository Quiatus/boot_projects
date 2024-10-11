import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


def main():

  pygame.init()
  pygame.font.init()
  game_font = pygame.font.SysFont("DejaVuSansMono", 32)

  print(pygame.font.get_default_font())

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  fps = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  Shot.containers = (shots, updatable, drawable)

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for obj in updatable:
      obj.update(dt)

    for asteroid in asteroids:
      if asteroid.collides_with(player):
        if player.get_shield() > 1:
          player.remove_shield()
          asteroid.kill()
          player.set_score()
        elif not player.get_shield() and player.get_life() > 25:
          player.remove_life()
          asteroid.kill()
          player.set_score()
        else:
          print(f"Game over! Your score is: {player.get_score()}")
          sys.exit()

      for shot in shots:
        if asteroid.collides_with(shot):
          shot.kill()
          asteroid.split()
          player.set_score()

    screen.fill("black")

    for obj in drawable:
      obj.draw(screen)

    text_score = game_font.render(f'Score: {player.get_score()}', True, (255,215,0))
    text_life = game_font.render(f'Hull: {player.get_life()}%', True, (220,20,60))
    text_shield = game_font.render(f'Shield: {player.get_shield()}%', True, (0,191,255))
    screen.blit(text_score, (5,5))
    screen.blit(text_life, (155,5))
    screen.blit(text_shield, (305,5))

    pygame.display.flip()

    dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()