import pygame
from pygame.locals import *
from core import *

clock = pygame.time.Clock()

if __name__ == '__main__':
	spaceship_group = pygame.sprite.Group()
	bullet_group = pygame.sprite.Group()
	spaceship = Spaceship(x=int(SCREEN_WIDTH / 2), y=SCREEN_HEIGHT - 100, health=3)
	spaceship_group.add(spaceship)

	bg = pygame.image.load(IMAGE_BACKGROUND)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	pygame.display.set_caption(TITLE_APP)

	run = True

	while run:
		clock.tick(FPS)
		screen.blit(bg, (0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		spaceship.update(screen)
		spaceship_group.draw(screen)
		bullet_group.draw(screen)
		pygame.display.update()

	pygame.quit()
