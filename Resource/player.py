import pygame
from .projectile import Projectile
from .tilemap import TILE_SIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, projectile_group, platforms):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.projectile_group = projectile_group
        self.platforms = platforms

        self.speed = 15
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_power = -12
        self.on_ground = False

    def update(self, keys):
        dx = 0
        if keys[pygame.K_a]:
            dx = -self.speed
        elif keys[pygame.K_d]:
            dx = self.speed

        self.rect.x += dx
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                elif dx < 0:
                    self.rect.left = platform.rect.right

        self.velocity_y += self.gravity
        if self.velocity_y > 20:
            self.velocity_y = 20
        self.rect.y += self.velocity_y

        self.on_ground = False
        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power

    def shoot(self, target_pos):
        projectile = Projectile(self.rect.center, target_pos)
        self.projectile_group.add(projectile)
