import pygame
from .tilemap import TILE_SIZE

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((50, 200, 50))
        self.rect = self.image.get_rect(topleft=(x, y))