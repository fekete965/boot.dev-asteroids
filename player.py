import pygame

from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHAPE_COLOR, SHAPE_LINE_WIDTH
from circleshape import CircleShape
from bullet import Bullet

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    
    return [a, b, c]
  
  def draw(self, screen):
    points = self.triangle()
    pygame.draw.polygon(screen, SHAPE_COLOR, points, SHAPE_LINE_WIDTH)
    
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt
    
  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt
    
  def shoot(self, dt):
    bullet = Bullet(self.position.x, self.position.y)
    bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

  def update(self, dt):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
      self.rotate(dt)
    if keys[pygame.K_d]:
      self.rotate(-dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)
    if keys[pygame.K_SPACE]:
      self.shoot(dt)
