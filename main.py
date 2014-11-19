import pygame
import random
from player import Player
from coin import Coin

pygame.init()

size = (500, 500)
bg_color = (255, 255, 255)
fps = 60

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
done = False

player = Player()
sprites = pygame.sprite.RenderPlain( (player) )
pygame.key.set_repeat(1, fps/2)

from random import randint
coins = pygame.sprite.Group()

def addcoin():
	coin = Coin()
	coin.rect.x = randint(0, 500)
	coin.rect.y = randint(0, 500)
	coins.add(coin)

for i in range(0,10):
	addcoin()

font = pygame.font.Font(None, 24) # second is size of font

MAX_COINS = 30

while not done:
	screen.fill(bg_color)
	hit = pygame.sprite.spritecollide(player, coins, True) # true removes coin

	choices = [(True, 1), (False, 100)]
	weighted = [val for val, cnt in choices for i in range(cnt)]

	if random.choice(weighted) and len(coins.sprites())<MAX_COINS:
		addcoin()

	for c in coins.sprites():
		c.float()
	
	coins.draw(screen) # ADDED
	
	player.give_money( len(hit) )

	text = font.render(str(player.coins), 1, (0,0,0) ) # antialias, color
	screen.blit(text, text.get_rect()) # draws it on screen

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player.move_down()

			if event.key == pygame.K_LEFT:
				player.move_left()
			
			if event.key == pygame.K_RIGHT:
				player.move_right()
			
			if event.key == pygame.K_UP:
				player.move_up()

		elif event.type == pygame.KEYUP:
			pass

		elif event.type == pygame.MOUSEMOTION:
			pass

		elif event.type == pygame.MOUSEBUTTONUP:
			pass

		elif event.type == pygame.MOUSEBUTTONDOWN:
			pass


	sprites.draw(screen)
	clock.tick(fps)
	pygame.display.flip()

pygame.quit()
