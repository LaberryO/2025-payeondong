import pygame
from .tilemap import TILE_SIZE

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((50, 200, 50))
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.topleft = (x, y)  # 월드 좌표로 위치 잡음
