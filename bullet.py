import pygame

from constants import BULLET_RADIUS, SHAPE_COLOR, SHAPE_LINE_WIDTH
from circleshape import CircleShape

class Bullet(CircleShape):
  init_sound_effect: pygame.mixer.Sound | None = None
  
  def __init__(self, x, y,):
    super().__init__(x, y, BULLET_RADIUS)
    
    if self.init_sound_effect is not None:
      self.init_sound_effect.set_volume(0.35)
      self.init_sound_effect.play()
    
  def draw(self, screen):
    pygame.draw.circle(screen, SHAPE_COLOR, self.position, self.radius, SHAPE_LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt
