import pygame
from core import IMAGE_BULLET


class Bullets(pygame.sprite.Sprite):
	def __init__(self, x: int, y: int):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(IMAGE_BULLET)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.y -= 5
