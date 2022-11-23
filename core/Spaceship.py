import pygame
from .settings import SCREEN_WIDTH, RED, GREEN


class Spaceship(pygame.sprite.Sprite):
	def __init__(self, image: str, x: int, y: int, health: int):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health

	def update(self, screen):
		speed = 8

		key = pygame.key.get_pressed()

		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= speed
		if key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
			self.rect.x += speed

		color = RED
		width = self.rect.width

		if self.health_remaining > 0:
			color = GREEN
			width = int(width * (self.health_remaining / self.health_start))

		pygame.draw.rect(
			screen,
			color,
			(self.rect.x, (self.rect.bottom + 10), width, 15)
		)

