import pygame
import random

class Coin(pygame.sprite.Sprite):
  image = None
  rect = None
  start_y = None
  shift_y = 8
  movement = 1
  up = None

  def __init__(self):
    random.choice([True,False])
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('coin.png').convert_alpha()
    self.rect = self.image.get_rect()

  def float(self):
    if random.choice([False,True]):
      return

    if self.start_y is None:
      self.start_y = self.rect.y

    if self.rect.y <= self.start_y - self.shift_y:
      self.up = False
    elif self.rect.y >= self.start_y + self.shift_y:
      self.up = True

    if self.up is True:
      self.rect.y = self.rect.y - self.movement
    else:
      self.rect.y = self.rect.y + self.movement
