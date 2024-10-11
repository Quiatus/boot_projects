import pygame

from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.rpm = 0
    self.score = 0
    self.life = PLAYER_START_LIFE
    self.shield = PLAYER_START_SHIELD

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen):
    pygame.draw.polygon(screen, (200,200,200), self.triangle(), 0)
    if self.shield:
      pygame.draw.circle(screen, (0,191,255), self.position, self.radius + 10, 2)

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
      keys = pygame.key.get_pressed()
      self.rpm -= dt

      if keys[pygame.K_w]:
          self.move(dt)

      if keys[pygame.K_s]:
          self.move(-dt)

      if keys[pygame.K_a]:
          self.rotate(-dt)
          
      if keys[pygame.K_d]:
          self.rotate(dt)

      if keys[pygame.K_SPACE]:
          self.shoot()

  
  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.rpm > 0:
       return
    self.rpm = PLAYER_SHOOT_COOLDOWN
    shot = Shot(self.position.x, self.position.y)
    shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

  def set_score(self):
    self.score += 1

  def get_score(self):
     return self.score
  
  def remove_life(self):
    self.life -= 25

  def get_life(self):
     return self.life
  
  def remove_shield(self):
    self.shield -= 25

  def get_shield(self):
     return self.shield

       
