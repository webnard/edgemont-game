import pygame

class Player(pygame.sprite.Sprite):
  image = None
  rect = None
  coins = 0

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load('pepper.png').convert_alpha()
    self.rect = self.image.get_rect()

  def move_up(self):
    self.rect.y = self.rect.y - 5
  
  def move_down(self):
    self.rect.y = self.rect.y + 5
  
  def move_left(self):
    self.rect.x = self.rect.x - 5
  
  def move_right(self):
    self.rect.x = self.rect.x + 5

  def give_money(self, amount):
    self.coins += amount
