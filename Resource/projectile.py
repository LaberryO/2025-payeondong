import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=start_pos)

        dx, dy = target_pos[0] - start_pos[0], target_pos[1] - start_pos[1]
        angle = math.atan2(dy, dx)
        self.speed = 10
        self.velocity = (math.cos(angle) * self.speed, math.sin(angle) * self.speed)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]