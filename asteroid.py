import random
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_MIN_ANGLE, ASTEROID_SPLIT_MAX_ANGLE, ASTEROID_SPLIT_VELOCITY_MULTIPLIER, SHAPE_COLOR, SHAPE_LINE_WIDTH

class Asteroid(CircleShape):
  kill_sound_effect: pygame.mixer.Sound | None = None
  
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def __get_new_angle(self):
    return random.uniform(ASTEROID_SPLIT_MIN_ANGLE, ASTEROID_SPLIT_MAX_ANGLE)

  def __create_asteroid_for_split(self, angle):
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    base_velocity = self.velocity.rotate(angle)
    
    new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid.velocity = base_velocity * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
    
    
  def draw(self, screen):
    pygame.draw.circle(screen, SHAPE_COLOR, self.position, self.radius, SHAPE_LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt
    
  def split(self):
    self.kill()
    
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    angle = self.__get_new_angle()
    self.__create_asteroid_for_split(angle)
    self.__create_asteroid_for_split(-angle)

  def kill(self):
    super().kill()
    
    if self.kill_sound_effect is not None:
      self.kill_sound_effect.set_volume(0.25)
      self.kill_sound_effect.play()
